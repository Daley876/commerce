from django.db import models
from auctions.models import User
from datetime import datetime
from django.utils import timezone
from createList.models import Listing
# Create your models here.


class Bids(models.Model):
    listingID = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bidList", default=1)
    bidBy = models.ForeignKey(User, on_delete=models.CASCADE,related_name="bidUser", default=1)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    datetimeOfBid = models.DateTimeField()


class Comment(models.Model):
    listingID = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="commentList", default=1)
    commentBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentUser", default=1)
    commentMade = models.CharField(max_length=500)
    datetimeOfComment = models.DateTimeField()


# THIS MODEL IS FOR STORING HISTORICAL DATA FOR CLOSED POSTS

class hist_lists(models.Model):
    listingID = models.CharField(max_length=40, primary_key=True)
    startingBid = models.FloatField(max_length=40)
    finalBid = models.FloatField(max_length=40)
    finalBidBy = models.CharField(max_length=40)
    listBy = models.CharField(max_length=40)
    closedDateTime = models.DateTimeField()


def __str__(self):
    return f"ID:{self.id},List ID:{self.listingID},Bid By: {self.bidBy}, Amount:{self.amount}"
