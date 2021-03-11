from django.shortcuts import render
from createList.models import Listing
from auctions.models import User
from watchlist.models import watcherList
from .models import Bids, hist_lists, Comment
from django.db.models import Max
from django.contrib import messages
from django.contrib.auth import get_user
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/admin')
def postComment(request):
        userCommText = request.POST['userComment']
        postID = request.POST['postingID']


        listing = Listing.objects.get(id=postID)
        userPostingID = get_user(request).id
        userPosting = User.objects.get(id=userPostingID)
        cDate = datetime.now()
        Comment.objects.create(listingID=listing, commentBy=userPosting, commentMade=userCommText,
                               datetimeOfComment=cDate)
        return HttpResponseRedirect(reverse("listings:index",args=(postID,)))


@login_required(login_url='/admin')
def createBid(request):
    fromForm = request.POST['bidAmt']
    idNum = request.POST['listingID']
    bid = float(fromForm)
    listId = str(idNum)

    listIdNum = Listing.objects.get(id=listId)  # list object
    userId = get_user(request).id
    UserID = User.objects.get(id=userId)  # user object

    maxBid = listIdNum.bid
    startBid = listIdNum.startingBid

    # validation for bid amount
    if UserID != listIdNum.userID:
        if bid >= startBid and bid > maxBid:
            # checks if user has current bid on item
            if Bids.objects.filter(listingID=listIdNum, bidBy=UserID).exists():
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
                cDate = datetime.now()
                Bids.objects.create(listingID=listIdNum, bidBy=UserID, amount=bid,datetimeOfBid=cDate)

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
    if not hist_lists.objects.filter(finalBidBy=userID, listingID=idNo).exists():

        # checks if listing ID in URL exists. i.e. listing is open
        if Listing.objects.filter(id=idNo).exists():
            listing = Listing.objects.get(id=idNo)

            user = User.objects.get(id=userID)
            totBids = Bids.objects.filter(listingID=listing)

            # sets messages to show about bids. total and if user has current max bid
            bidsCount = str(totBids.count())
            numBids = bidsCount + " bid(s) so far."
            ownerCheck = ""
            bidMsgCheck = ""

            if listing.userID == user:
                ownerCheck = "set"

            ownedListing = ownerCheck

            if user == listing.currBidBy and totBids.filter(listingID=listing,bidBy=user).exists():
                bidMsgCheck = " Your bid is the current bid."
            bidMsg = bidMsgCheck


            try:
                watchedItemsCounter = watcherList.objects.filter(watchedBy=user).count()
            except:
                watchedItemsCounter= 0

            try:
                #  gets all comments on listing
                listingComments = Comment.objects.filter(listingID=listing)
                listingComments_sorted = listingComments.order_by('-id')
            except:
                listingComments_sorted = ""
            try:
                #  check if listing is on watchlist
                watcheditems = watcherList.objects.get(listID=listing, watchedBy=user)
            except:
                watcheditems = ""  # this assigns null to variable in the event no rows exist

            return render(request, "listings/index.html", {
                "posting": listing, "items": watcheditems, "numBids": numBids,
                "bidMsg": bidMsg, "ownedListing": ownedListing, "currComments":listingComments_sorted,
                "watchedItems":watchedItemsCounter
            })
        else:
            user = User.objects.get(id=userID)
            try:
                watchedItemsCounter = watcherList.objects.filter(watchedBy=user).count()
            except:
                watchedItemsCounter= 0

        return render(request, "listings/index.html", {
                "closedMsg": "THIS LISTING IS NO LONGER AVAILABLE.",
            "watchedItems":watchedItemsCounter
            })

    else:
        user = User.objects.get(id=userID)
        try:
            watchedItemsCounter = watcherList.objects.filter(watchedBy=user).count()
        except:
            watchedItemsCounter= 0

    return render(request, "listings/index.html", {
            "winMsg": "CONGRATULATIONS! YOUR BID WON THIS LISTING!",
            "watchedItems":watchedItemsCounter
        })


#  ADDS ITEM FROM WATCH LIST
@login_required(login_url='/admin')
def addToWatchList(request):
    idNum = request.POST['listingIDwatch']
    # finalID = int(idNum)
    listing = Listing.objects.get(id=idNum)
    watchUser = get_user(request)
    Adduser = User.objects.get(id=listing.userID.id)
    watcherList.objects.create(listID=listing, addedBy=Adduser, watchedBy=watchUser)
    return HttpResponseRedirect(reverse("listings:index", args=(idNum,)))


#  REMOVES ITEM FROM WATCH LIST
@login_required(login_url='/admin')
def DelFromWatchList(request):
    idNum = request.POST['listingIDwatch']
    listing = Listing.objects.get(id=idNum)
    watchUser = get_user(request).id
    Adduser = User.objects.get(id=listing.userID.id)
    watcherList.objects.get(listID=listing, addedBy=Adduser, watchedBy=watchUser).delete()
    return HttpResponseRedirect(reverse("listings:index", args=(idNum,)))


#  CLOSES LISTING
@login_required(login_url='/admin')
def closeListing(request):
    idNum = request.POST['postingID']
    listObject = Listing.objects.get(id=idNum)
    cDate = datetime.now()
    # archives post before deleting.
    hist_lists.objects.create(listingID=idNum, startingBid=listObject.startingBid, finalBid=listObject.bid,
                              finalBidBy=listObject.currBidBy, listBy=listObject.userID,closedDateTime=cDate)
    listObject.delete()
    userID = get_user(request).id
    user = User.objects.get(id=userID)
    try:
        watchedItemsCounter = watcherList.objects.filter(watchedBy=user).count()
    except:
        watchedItemsCounter= 0

    return render(request, "listings/index.html", {
        "closedMsg": "THIS LISTING HAS BEEN CLOSED.",
        "watchedItems":watchedItemsCounter
    })
