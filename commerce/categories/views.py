from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import get_user
from watchlist.models import watcherList
from auctions.models import User
from django.http import HttpResponseRedirect
from createList.models import Category,Listing
# Create your views here.

def Categories(request):
    idNo = get_user(request).id
    user_code = User.objects.get(id=idNo)

    try:
        watchedItemsCounter = watcherList.objects.filter(watchedBy=user_code).count()
    except:
        watchedItemsCounter= 0
    return render(request,"categories/index.html",{
        "cat_list":Category.objects.all(),  "watchedItemsCounter":watchedItemsCounter
    })

def CategoryView(request,categoryName):
    idNo = get_user(request).id
    user_code = User.objects.get(id=idNo)
    try:
        watchedItemsCounter = watcherList.objects.filter(watchedBy=user_code).count()
    except:
        watchedItemsCounter= 0

# this statement searches Category table by NAME but only returns the CODE field.
    cat_code = Category.objects.filter(name=categoryName).values_list('code')

    return render(request,"categories/viewCat.html",{
        "cat":categoryName, "listings":Listing.objects.filter(category_name__in=cat_code),
        "watchedItemsCounter":watchedItemsCounter
        #  __in on the category_name field is used to handle result sets greateer than 1
    })