from django.shortcuts import render
from createList.models import Listing
from auctions.models import User
from watchlist.models import watcherList
from .models import Bids, hist_lists
from django.db.models import Max
from django.contrib import messages
from django.contrib.auth import get_user
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/admin')
def createBid(request):
    fromForm = request.POST['bidAmt']
    idNum = request.POST['listingID']
    bid = float(fromForm)
    listId = str(idNum)
    now = datetime.now()  # get system date
    createDate = now.strftime("%B %d, %Y %I:%M %p")  # formats date to string and saves

    listIdNum = Listing.objects.get(id=listId)  # list object
    userId = get_user(request).id
    UserID = User.objects.get(id=userId)  # user object

    maxBid = listIdNum.bid
    startBid = listIdNum.startingBid

    # validation for bid amount
    if (UserID != listIdNum.userID):
        if (bid >= startBid and bid > maxBid):
            # checks if user has current bid on item
            if (Bids.objects.filter(listingID=listIdNum, bidBy=UserID).exists()):
                curr_bid = Bids.objects.get(listingID=listIdNum, bidBy=UserID)
                curr_bid.amount = bid
                curr_bid.save()
                # updates current listing with new bid amount
                listIdNum.bid = bid
                listIdNum.save()
                listIdNum.currBidBy = UserID
                listIdNum.save()
                messages.info(request, "Your bid has been placed.")
                return HttpResponseRedirect(reverse("listings:index", args=(listId,)))
            else:
                # gets listing from db based on ID number
                Bids.objects.create(listingID=listIdNum, bidBy=UserID, amount=bid, datetimeOfBid=createDate)

                # updates current listing with new bid amount
                listIdNum.bid = bid
                listIdNum.save()
                listIdNum.currBidBy = UserID
                listIdNum.save()
                messages.info(request, "Your bid has been placed.")
                return HttpResponseRedirect(reverse("listings:index", args=(listId,)))
        else:
            messages.error(request, "This bid cannot be placed. Please adjust bid amount.")
            return HttpResponseRedirect(reverse("listings:index", args=(listId,)))
    else:
        messages.error(request, "Cannot bid on own listing.")
        return HttpResponseRedirect(reverse("listings:index", args=(listId,)))


# This function lists full details of an item. it will search for item from watchList table automatically
# if no item is found null is sent to template and Button becomes "Add to list"
# if item is found then it is sent to template and Button becomes "Remove to list"

@login_required(login_url='/admin')
def listingsView(request, idNo):
    userID = get_user(request).id
# checks user won listing or not
    if (not hist_lists.objects.filter(finalBidBy=userID,listingID=idNo).exists()):
        #checks if listing ID in URL exists
        if (Listing.objects.filter(id=idNo).exists()):
            listing = Listing.objects.get(id=idNo)

            user = User.objects.get(id=userID)

            # sets messages to show about about bids. total and if user has current max bid
            bidsCount = str(Bids.objects.count())
            numBids = bidsCount + " bid(s) so far."
            bidMsgCheck = ""
            ownerCheck = ""

            if listing.userID == user:
                ownerCheck = "set"
            ownedListing = ownerCheck

            if user == listing.currBidBy:
                bidMsgCheck = " Your bid is the current bid."
            bidMsg = bidMsgCheck

            try:

                watcheditems = watcherList.objects.get(listID=listing, watchedBy=user)
            except:
                watcheditems = ""  # this assigns null to variable in the event no rows exist
                return render(request, "listings/index.html", {
                    "posting": listing, "items": watcheditems, "numBids": numBids,
                    "bidMsg": bidMsg, "ownedListing": ownedListing
                })

            return render(request, "listings/index.html", {
                "posting": listing, "items": watcheditems, "numBids": numBids,
                "bidMsg": bidMsg, "ownedListing": ownedListing
            })
        else:
            return render(request, "listings/index.html", {
                "closedMsg": "THIS LISTING IS NO LONGER AVAILABLE."
            })

    else:
        return render(request, "listings/index.html", {
            "winMsg": "CONGRATULATIONS! YOUR BID FOR THIS LISTING WON!"
        })

#  ADDS ITEM FROM WATCH LIST
@login_required(login_url='/admin')
def addToWatchList(request):
    idNum = request.POST['listingIDwatch']
    print(idNum)
    # finalID = int(idNum)
    list = Listing.objects.get(id=idNum)
    watchUser = get_user(request)
    Adduser = User.objects.get(id=list.userID.id)
    watcherList.objects.create(listID=list, addedBy=Adduser, watchedBy=watchUser)
    return HttpResponseRedirect(reverse("listings:index", args=(idNum,)))


#  REMOVES ITEM FROM WATCH LIST
@login_required(login_url='/admin')
def DelFromWatchList(request):
    idNum = request.POST['listingIDwatch']
    # finalID = int(idNum)
    list = Listing.objects.get(id=idNum)
    watchUser = get_user(request).id
    Adduser = User.objects.get(id=list.userID.id)
    watcherList.objects.get(listID=list, addedBy=Adduser, watchedBy=watchUser).delete()
    return HttpResponseRedirect(reverse("listings:index", args=(idNum,)))


#  REMOVES ITEM FROM LISTINGS
@login_required(login_url='/admin')
def closeListing(request):
    idNum = request.POST['postingID']
    listObject = Listing.objects.get(id=idNum)

    now = datetime.now()  # get system date
    closedDate = now.strftime("%B %d, %Y %I:%M %p")  # formats date to string and saves

    # archives post before deleting.
    hist_lists.objects.create(listingID=idNum, startingBid=listObject.startingBid, finalBid=listObject.bid,
                              finalBidBy=listObject.currBidBy, listBy=listObject.userID,
                              closedDateTime=closedDate)
    listObject.delete()
    return render(request, "listings/index.html", {
        "closedMsg": "THIS LISTING IS NO LONGER AVAILABLE."
    })
