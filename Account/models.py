from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    Avatar = models.ImageField( upload_to="user/avatar", blank=True , null=True)
    username = models.CharField( max_length=100 , null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["Avatar" ,"username"]

    def __str__(self):
        return self.username


class Subscriber(models.Model):
    username = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

