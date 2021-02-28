from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django import forms
from .models import  Listing, Category
# Create your views here.

class createListingForm(forms.Form):
    cat = Category.objects.all()
    title = forms.CharField(label="Title",max_length=36)
    description = forms.CharField(label="Description",
                widget=forms.Textarea(attrs={'style': 'resize:none'}))
    bid = forms.FloatField()
    url = forms.CharField(max_length=250)
    category = forms.ChoiceField(choices=cat)


def createListing(request):
    if request.method == "POST":
        form = createListingForm(request.POST)
        if form.is_valid():

            newBid = form.cleaned_data["bid"]
            newUrl = form.cleaned_data["url"]
            newTitle = form.cleaned_data["title"]
            newDesc = form.cleaned_data["description"]
            newCat = form.cleaned_data["category"]

            Listing.objects.create(title=newTitle,description=newDesc,bid=newBid,url=newUrl
                                   ,code=Category.objects.get(newCat)
                                )
            return HttpResponseRedirect(reverse("index"))


    else:
        return render(request, "createList/createListing.html", {
            "user":request.user, "form":createListingForm
        })

