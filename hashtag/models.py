from django.db import models
from django.urls import reverse
# Create your models here.

class Hashtag(models.Model):
    hashtag=models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hashtag

    def get_absolute_url(self):
        return reverse("tags:tag",kwargs={'tag':self.hashtag})

