from django.urls import path

from . import views
# IT IS IMPORT TO REMEMBER THAT URL WITH ARGUMENTS CAN NEVER BE IDENTICAL. EVEN IF NAME ATTR IS DIFFERENT
app_name = "listings"
urlpatterns = [
    path("", views.listingsView, name="index"),
    path("<int:idNo>", views.listingsView, name="index"),
    path("", views.addToWatchList, name="add"),
    path("add_to_list",views.addToWatchList,name="add"),
    path("", views.addToWatchList, name="del"),
    path("remove_to_list",views.DelFromWatchList,name="del")

]