from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipt(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    store_name = models.CharField(max_length=150)
    purchase_date = models.DateTimeField(null=True,blank=True,default=datetime.now)
    item_list = models.TextField()
    total = models.IntegerField()