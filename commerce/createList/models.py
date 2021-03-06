from django.db import models
from auctions.models import User
# Create your models here.

class Category (models.Model):
    code = models.CharField(max_length=4,primary_key=True)
    name = models.CharField(max_length=40,unique=True)
    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    title = models.CharField(max_length=36)
    description = models.TextField()
    bid = models.FloatField()
    startingBid = models.FloatField(default=0.00)
    currBidBy = models.ForeignKey(User, on_delete=models.CASCADE,related_name="currBidUser",default=1)
    url = models.TextField(max_length=250,blank=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,default="NONE",related_name="cats")
    userID = models.ForeignKey(User, on_delete=models.CASCADE,related_name="createUser",default=1)
    createDateTime = models.CharField(max_length=60,default="NONE")

    def __str__(self):
        return f"{self.id}"

