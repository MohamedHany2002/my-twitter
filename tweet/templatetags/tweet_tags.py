from django import template
from tweet.models import Tweet
from hashtag.models import Hashtag
from django.shortcuts import get_object_or_404


register=template.Library()

def func(text):
    tag=text.split(' ')[0]
    m=Hashtag.objects.filter(hashtag=tag)
    if m:
        myobj=m.first()
        return myobj
    else:
        return False

@register.filter
def hash(text):
    words=text.split(' ')
    for i in range(len(text)):
        if text[i]=='#':
            newstring=text[i+1:]
            obj=func(newstring)
            if obj:
                return obj.get_absolute_url()
    return text


        
