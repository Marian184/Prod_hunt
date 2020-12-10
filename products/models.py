from django.db import models

# Create your models here.
class Product(models.Model):

    title = models.CharField(max_length=255, default="")
    url = models.CharField(max_length=255, default="")
    pub_date = models.DateTimeField()

    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='icon/')
