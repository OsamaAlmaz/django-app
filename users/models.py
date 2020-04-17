from django.db import models

# Create your models here.

#want the backend to store the users. 
class Users(models.Model):
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    dateofbirth = models.DateField()
    email = models.TextField(max_length = 40)
    username = models.CharField(max_length = 30)
    password = models.TextField(max_length = 30) 
    repeat_password = models.TextField(max_length = 30)
    