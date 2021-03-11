from django.contrib import admin

from .models import Bids, hist_lists, Comment
# Register your models here.


class Hist_List_Admin(admin.ModelAdmin):
    list_display = ("listingID", "startingBid", "finalBid", "finalBidBy", "listBy", "closedDateTime")


class BidsAdmin(admin.ModelAdmin):
    list_display = ("id", "listingID", "bidBy", "amount", "datetimeOfBid")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "listingID", "commentBy", "commentMade", "datetimeOfComment")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Bids, BidsAdmin)
admin.site.register(hist_lists, Hist_List_Admin)
