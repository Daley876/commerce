from django.urls import path

from . import views

app_name = "creation"
urlpatterns = [
    path("", views.createListing, name="create"),
    path("<int:idNo>", views.createListing, name="create")
]
