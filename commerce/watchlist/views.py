from django.shortcuts import render
from auctions.models import User
from createList.models import Listing
from .models import watcherList
from django.contrib.auth import get_user
from auctions.views import login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/admin')
def watchlistView (request,idNo):
    if (get_user(request)):
        # gets user object based on userID
        user_code = User.objects.get(id=idNo)

        #searches watch list table for users with corresponding ID. retrieves list code
        list_code = watcherList.objects.filter(watchedBy=user_code).values_list("listID")

    # gets all listings with list_code taken from wacth list table
        return render(request,"watchlist/index.html",{
            "postings":Listing.objects.filter(id__in=list_code)})
    else:
        return HttpResponseRedirect(reverse("auctions:login",))


