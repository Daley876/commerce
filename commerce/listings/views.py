from django.shortcuts import render
from createList.models import Listing
from auctions.models import User
from django.contrib.auth import get_user
from watchlist.models import watcherList
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

#This function lists full details of an item. it will search for item from watchList table automatically
# if no item is found null is sent to template and Button becomes "Add to list"
#if item is found then it is sent to template and Button becomes "Remove to list"
@login_required(login_url='/admin')
def listingsView(request,idNo):
    listing = Listing.objects.get(id=idNo)

    try:
        userID = get_user(request).id
        user = User.objects.get(id=userID)
        watcheditems = watcherList.objects.get(listID=listing,watchedBy=user)
    except:
        watcheditems = ""
        return render(request, "listings/index.html", {
            "posting":listing,"items":watcheditems
        })

    return render(request, "listings/index.html", {
        "posting":listing,"items":watcheditems
    })


#  ADDS ITEM FROM WATCH LIST
@login_required(login_url='/admin')
def addToWatchList(request):
    idNum = request.POST['listingID']
    finalID = str(idNum)
    list = Listing.objects.get(id=finalID)
    watchUser = get_user(request)
    Adduser = User.objects.get(id=list.userID.id)
    watcherList.objects.create(listID=list,addedBy=Adduser,watchedBy=watchUser)
    return HttpResponseRedirect(reverse("listings:index",args=(idNum)),)



#  REMOVES ITEM FROM WATCH LIST
@login_required(login_url='/admin')
def DelFromWatchList(request):
    idNum = request.POST['listingID']
    finalID = str(idNum)
    list = Listing.objects.get(id=finalID)
    watchUser = get_user(request).id
    Adduser = User.objects.get(id=list.userID.id)
    watcherList.objects.get(listID=list,addedBy=Adduser,watchedBy=watchUser).delete()
    return HttpResponseRedirect(reverse("listings:index",args=(idNum)),)