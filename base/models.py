from django.db import models
# myapp/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name=models.CharField(max_length=30,null=False)
    phone=models.IntegerField(max_length=10,null=False,default=None)
    
class CitizenUser(CustomUser):
    pass

class StaffUser(CustomUser):
    staff_id=models.CharField(max_length=6,primary_key=True)
    position=models.CharField(max_length=10,null=False)
