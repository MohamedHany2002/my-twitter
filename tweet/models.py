from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .utils import validateText
from django.urls import reverse
from hashtag.models import Hashtag
from django.db.models.signals import pre_save,post_save


# Create your models here.


class retweetManager(models.Manager):


    def retweet(self,tweet,user):
        obj=self.model(parent=tweet,user=user)



class Tweet(models.Model):
    parentTweet = models.ForeignKey('self',on_delete=models.CASCADE,related_name='parenttweets',null=True,blank=True)
    text = models.CharField(max_length=140,validators=[validateText])
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tweets')
    created = models.DateTimeField(auto_now_add=True)
    hashtag = models.ForeignKey(Hashtag,blank=True,null=True,on_delete=models.CASCADE,related_name='tweets')
    
    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def get_hash_url(self):
        return reverse("hash",{'hashtag':self.hashtag})

    def isHash(self):
        if self.hashtag:
            return True
        return False

    class Meta:
        ordering=('-created',)

def save_hashtags(sender,**kwargs):
    print('nice')
    text = kwargs['instance'].text
    mine=''
    ts=''

    def func(text):
        myhashtag=text.split(' ')[0]
        
        print(myhashtag)
        newHashtag,created=Hashtag.objects.get_or_create(hashtag=myhashtag)
        kwargs['instance'].hashtag=newHashtag
        # kwargs['instance'].save()
                

    for i in range(len(text)):
        if text[i] == '#':
            print(text[i])
            newText=text[i+1:]
            
            print(newText)
            func(newText)
            break;
pre_save.connect(save_hashtags,sender=Tweet)











def tweetHashtags(sender,**kwargs):
    print(kwargs['instance'])
    for hash in hash_list:
        kwargs['instance'].hashtags.add(hash)
























    # print(kwargs['instance'].hashtags.all())

# post_save.connect(tweetHashtags,sender=Tweet)

    # def clean(self,*args,**kwargs):
    #     if self.text=="abc":
    #         raise ValidationError("wrong")
    #     return super(Tweet,self).clean(*args,**kwargs)
