from django.urls import path

from . import views

app_name = "categories"
urlpatterns = [
    path("", views.Categories, name="index"),
    path("", views.CategoryView, name="catView"),
    path("<str:categoryName>", views.CategoryView, name="catView")
]