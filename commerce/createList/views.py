from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import get_user
from watchlist.models import watcherList
from auctions.models import User
from .models import  Listing, Category
from django.contrib.auth.decorators import login_required
# Create your views here.

class createListingForm(forms.Form):
    newTitle = forms.CharField(label="Title: ",max_length=36)
    newDesc = forms.CharField(label="Description: ",
                widget=forms.Textarea(attrs={'style': 'resize:none'}))
    newBid = forms.FloatField(label="Bid: ",widget=forms.CharField.widget)
    newUrl = forms.CharField(max_length=250,label="Image URL (optional): ",required=False)
    # forms.modelChoiceField is used for select object options
    newCat = forms.ModelChoiceField(label="Category: ",queryset=Category.objects.all(),
                                    to_field_name="name",
                                    initial=Category.objects.get(code="NONE"))

@login_required(login_url='/admin')
def createListing(request,idNo):
    user = User.objects.get(id=idNo)
    try:
        watchedItemsCounter = watcherList.objects.filter(watchedBy=user).count()
    except:
        watchedItemsCounter= 0
    if request.method == "POST":
        form = createListingForm(request.POST)
        if form.is_valid():

            newBid = form.cleaned_data["newBid"]
            newUrl = form.cleaned_data["newUrl"]
            newTitle = form.cleaned_data["newTitle"]
            newDesc = form.cleaned_data["newDesc"]
            newCat = form.cleaned_data["newCat"]
            cDate = datetime.now()

# when retrieving a single row, use get. this returns an object as opposed to a result set
            UserIdNum = User.objects.get(id=idNo)

            #saves new listing
            Listing.objects.create(title=newTitle,description=newDesc,bid=newBid,
                                   startingBid=newBid,url=newUrl,
                                   category_name=newCat,userID=UserIdNum,createDateTime=cDate)
            return HttpResponseRedirect(reverse("auctions:index"))


    else:
        return render(request, "createList/createListing.html", {"form":createListingForm,
                "watchedItemsCounter":watchedItemsCounter})

