from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import  Listing, Category
# Create your views here.

class createListingForm(forms.Form):
    newTitle = forms.CharField(label="Title",max_length=36)
    newDesc = forms.CharField(label="Description",
                widget=forms.Textarea(attrs={'style': 'resize:none'}))
    newBid = forms.FloatField(label="Bid",)
    newUrl = forms.CharField(max_length=250,label="URL",)
    # forms.modelChoiceField is used for select object options
    newCat = forms.ModelChoiceField(label="Category",queryset=Category.objects.all(),
                                    to_field_name="name",
                                    initial=Category.objects.get(code="NONE"))


def createListing(request):
    if request.method == "POST":
        form = createListingForm(request.POST)
        if form.is_valid():

            newBid = form.cleaned_data["newBid"]
            newUrl = form.cleaned_data["newUrl"]
            newTitle = form.cleaned_data["newTitle"]
            newDesc = form.cleaned_data["newDesc"]
            newCat = form.cleaned_data["newCat"]

#saves new listing
            Listing.objects.create(title=newTitle,description=newDesc,bid=newBid,url=newUrl,
                                   category_name=newCat)
            return HttpResponseRedirect(reverse("auctions:index"))


    else:
        return render(request, "createList/createListing.html", {
            "user":request.user, "form":createListingForm
        })

