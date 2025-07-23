from django.db import models
from Account.models import Profile

class Cartegory(models.Model):
    cartegory = models.CharField( max_length=100)
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cartegory

class NewsContent(models.Model):
    Title = models.CharField( max_length=200)
    Cartegory = models.ForeignKey("Cartegory",  on_delete=models.CASCADE)
    Picture = models.ImageField(upload_to="News/Stories" ,null=True , blank=True)
    Story = models.TextField()
    Host = models.ForeignKey(Profile , on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Title
    
class LatestNews(models.Model):
    Title = models.CharField( max_length=200)
    Cartegory = models.ForeignKey("Cartegory",  on_delete=models.CASCADE)
    Picture = models.ImageField(upload_to="News/Latest" ,null=True , blank=True)
    Story = models.TextField()
    Host = models.ForeignKey(Profile , on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Title