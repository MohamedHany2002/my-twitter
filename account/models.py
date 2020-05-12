from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db.models.signals import post_save
# Create your mo

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followings = models.ManyToManyField(User,related_name='followed_by',blank=True)

    def __str__(self):
        return self.user.username +str(self.followings.all().count())

    def get_absolute_url(self):
        return reverse_lazy("profile",kwargs={'username':self.user.username})
    
    def get_follow_url(self):
        return reverse_lazy("method",kwargs={'id':self.user.id})


def save_profile(sender,**kwargs):
    profile.objects.create(user=kwargs['instance'])
    kwargs['instance'].profile.followings.add(kwargs['instance'])
post_save.connect(save_profile,sender=User)

