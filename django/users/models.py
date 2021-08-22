from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Users(models.Model):
   
    name = models.TextField(max_length=30, blank=False)
    birthdate = models.DateField(null=True, blank=True)
    email= models.EmailField(max_length=50, blank=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
    instance.profile.save()
