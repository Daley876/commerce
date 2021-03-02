from django.urls import path

from . import views

app_name = "watchlist"
urlpatterns = [
    path("", views.watchlistView, name="index"),
    path("<int:idNo>", views.watchlistView, name="index")
]