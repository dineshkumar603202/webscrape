from django.db import models

# Create your models here.
class FetchModel(models.Model):
    url = models.URLField(max_length=200,null=True)
    title = models.CharField(max_length=128,null=True)
    description =  models.CharField(max_length=800,null=True)
    price = models.CharField(max_length=200,null=True)
    mobile_number = models.CharField(max_length=20,null=True)
    size = models.CharField(max_length=128,null=True)