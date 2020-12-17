from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Product(models.Model):

    title = models.CharField(max_length=255, default="")
    url = models.CharField(max_length=255, default="")
    pub_date = models.DateTimeField(null=True, blank=True)
    votes_total = models.IntegerField(default=1)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Voter(models.Model):
    voters = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                default=1)