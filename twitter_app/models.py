from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Tweet(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
