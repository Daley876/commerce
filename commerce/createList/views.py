from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from auctions.models import User
from .models import  Listing, Category
from django.contrib.auth.decorators import login_required
# Create your views here.

class createListingForm(forms.Form):
    newTitle = forms.CharField(label="Title",max_length=36)
    newDesc = forms.CharField(label="Description",
                widget=forms.Textarea(attrs={'style': 'resize:none'}))
    newBid = forms.FloatField(label="Bid",widget=forms.CharField.widget)
    newUrl = forms.CharField(max_length=250,label="URL",required=False)
    # forms.modelChoiceField is used for select object options
    newCat = forms.ModelChoiceField(label="Category",queryset=Category.objects.all(),
                                    to_field_name="name",
                                    initial=Category.objects.get(code="NONE"))

@login_required(login_url='/admin')
def createListing(request,idNo):
    if request.method == "POST":
        form = createListingForm(request.POST)
        if form.is_valid():

            newBid = form.cleaned_data["newBid"]
            newUrl = form.cleaned_data["newUrl"]
            newTitle = form.cleaned_data["newTitle"]
            newDesc = form.cleaned_data["newDesc"]
            newCat = form.cleaned_data["newCat"]

            now = datetime.now() # get system date
            createDate = now.strftime("%B %d, %Y %I:%M %p") #formats date to string and saves

# when retrieving a single row, use get. this returns an object as opposed to a result set
            UserIdNum = User.objects.get(id=idNo)

            #saves new listing
            Listing.objects.create(title=newTitle,description=newDesc,bid=newBid,url=newUrl,
                                   category_name=newCat,createDateTime=createDate,userID=UserIdNum)
            return HttpResponseRedirect(reverse("auctions:index"))


    else:
        return render(request, "createList/createListing.html", {"form":createListingForm
        })

