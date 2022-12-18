from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    name = models.CharField(max_length=100)
    likes = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Request_To_Chat(models.Model):
    username =  models.CharField(max_length=100)