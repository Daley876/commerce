from django.db import models
# Create your models here.

class Category (models.Model):
    code = models.CharField(max_length=4,primary_key=True)
    name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    title = models.CharField(max_length=36)
    description = models.TextField()
    bid = models.FloatField()
    url = models.TextField(max_length=250)
    code = models.ForeignKey(Category, on_delete=models.CASCADE,default="XXXX")
    def __str__(self):
        return f"ID: {self.id} Title:{self.title}, Desc:{self.description}, Bid:{self.bid}, URL:{self.url}," \
               f"Category:{self.code}"

