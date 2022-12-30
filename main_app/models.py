from django.db import models
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

# Create your models here.
class Fund(models.Model):
    name= models.CharField(max_length=100)
    qualification= models.CharField(max_length=500)
    description= models.CharField(max_length=500)
    deadline= models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    name= models.CharField(max_length=100)
    qualification= models.CharField(max_length=500)
    description= models.CharField(max_length=500)
    deadline= models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name  

class Activity(models.Model):
    applied= models.CharField(max_length=100, null=True)
    remindtoapply= models.CharField(max_length=100, null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.applied  
