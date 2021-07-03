from django.db import models

# Create your models here.

class Item(models.Model):
    ItemId  = models.AutoField(primary_key= True)
    ItemName = models.CharField(max_length = 100)
    ItemPrice = models.IntegerField()