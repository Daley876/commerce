from django.contrib import admin
from .models import Listing,Category
# Register your models here.

class CatAdmin(admin.ModelAdmin):
    list_display = ("code","name")
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id","title","description","bid","url","code") #  comma at the end is mandatory

admin.site.register(Listing,ListingAdmin)
admin.site.register(Category, CatAdmin)
