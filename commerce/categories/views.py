from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from createList.models import Category,Listing
# Create your views here.

def Categories(request):
    return render(request,"categories/index.html",{
        "cat_list":Category.objects.all()
    })

def CategoryView(request,categoryName):

# this statement searches Category table by NAME but only returns the CODE field.
    cat_code = Category.objects.filter(name=categoryName).values_list('code')

    return render(request,"categories/viewCat.html",{
        "cat":categoryName, "listings":Listing.objects.filter(category_name__in=cat_code)
        #  __in on the category_name field is used to handle result sets greateer than 1
    })