from django.shortcuts import render
from auctions.models import User
from createList.models import Listing
from .models import watcherList
# Create your views here.
def watchlistView (request,idNo):
    # gets user object based on userID
    user_code = User.objects.get(id=idNo)

    #searches watch list table for users with corresponding ID. retrieves list code
    list_code = watcherList.objects.filter(userID=user_code).values_list("listID")

# gets all listings with list_code taken from wacth list table
    return render(request,"watchlist/index.html",{
        "postings":Listing.objects.filter(id__in=list_code)
    })
