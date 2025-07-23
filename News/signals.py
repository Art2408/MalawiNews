from .models import NewsContent , LatestNews
from Account.models import Subscriber
from django.dispatch import receiver
from django.db.models.signals import post_delete,post_save

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import os


@receiver(post_save,sender=LatestNews,dispatch_uid="Notify_Subscribers")
def Notify_Subscribers(sender,instance , created,**kwargs):
    if created:
        print("Latest News created")
        body = render_to_string("email-temp.html",{"news_id":instance.id,"name":Subscriber.username})
        email = EmailMessage(
            instance.Title,
            body,
            "mcarthur@gmail.com",
            ["example@gmail.com"]
        )

        email.fail_silenty = False
        email.send()


@receiver(post_delete,sender=NewsContent)
def Delete_News_Images(sender,instance,**kwargs):
    if instance.Picture:
        if os.path.isfile(instance.Picture.path):
            os.remove(instance.Picture.path)
            print("image removed" ,instance.Picture.path)


@receiver(post_delete,sender=LatestNews)
def Delete_Latest_Images(sender,instance,**kwargs):
    if instance.Picture:
        if os.path.isfile(instance.Picture.path):
            os.remove(instance.Picture.path)
            print("image removed" ,instance.Picture.path)            