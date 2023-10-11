from asyncio.base_futures import _PENDING
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city= models.CharField(max_length=200)
    phone= models.CharField(max_length=12,default=0)
    email= models.CharField(max_length=50,default=None)
    country=models.CharField(max_length=50,default=None)
    amount=models.IntegerField(default=0)

class Plan(models.Model):
    plan_type= models.CharField(max_length=50,default=None)
    plan_per=models.CharField(max_length=50,default=None)
    profit=models.IntegerField(default=0)
    price=models.IntegerField(default=0)

 
class Deposit(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    amount=models.IntegerField(default=None)
    is_status=models.CharField(max_length=50,default="pending")

    
