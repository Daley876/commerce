from django.db import models
from createList.models import Listing
from auctions.models import User
# Create your models here.


class watcherList(models.Model):
    listID = models.ForeignKey(Listing,on_delete=models.CASCADE,default=1,related_name="lists")
    userID = models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name="users")

    def __str__(self):
        return f"ID:{self.id}, List ID:{self.listID}, User ID:{self.userID}"