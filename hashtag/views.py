from django.shortcuts import render
from .models import Hashtag

# Create your views here.

def visitTag(request,tag):
    m=Hashtag.objects.filter(hashtag=tag)
    x=m.first()
    print("ok")
    return render(request,"tweets/tag.html",{'tag':x})