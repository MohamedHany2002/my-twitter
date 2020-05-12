from django.shortcuts import render,reverse,get_object_or_404,HttpResponseRedirect
from .models import Tweet
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import tweetForm
from django import forms
from django.forms.utils import ErrorList
from .mixins import FormMixin,checkowner
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views here.

class createTweet(FormMixin,CreateView):
    form_class = tweetForm
    template_name = 'tweets/create.html'
    # success_url='/create/'
    login_url='/admin/'

class deleteTweet(DeleteView):
    model=Tweet
    success_url = reverse_lazy("home")
    template_name="tweets/confirm_delete.html"

class updateTweet(LoginRequiredMixin,checkowner,UpdateView):
    form_class=tweetForm
    model=Tweet
    template_name="tweets/update.html"
    # success_ur redddl="/"


class tweets(ListView):
    # queryset = Tweet.objects.all()
    template_name='tweets/list.html'
    def get_queryset(self):
        all_followings=self.request.user.profile.followings.values_list('id',flat=True)
        qs = Tweet.objects.filter(user_id__in=all_followings)
        query=self.request.GET.get('q',None)
        if query:
            qs=qs.filter(text__icontains=query)
        return qs

    def get_context_data(self, *args,**kwargs):
        context=super(tweets,self).get_context_data(*args, **kwargs)
        context['form']=tweetForm
        context['url']=reverse('create')
        return context

class tweet_detail(DetailView):
    # def get_object(self):
    #     return Tweet.objects.get(id=self.kwargs['id'])
    # queryset = Tweet.objects.all()
    model = Tweet
    template_name='tweets/detail.html'

def retweet(request,id):
    tweet=get_object_or_404(Tweet,id=id)
    if tweet.parentTweet:
        parent=get_object_or_404(Tweet,id=tweet.parentTweet.id)
        qs=Tweet.objects.filter(parentTweet=parent,user=request.user)
        if qs.exists():
            print('not created')
        else:
            print('creaetd')
            newTweet=Tweet.objects.create(parentTweet=tweet,text=tweet.text,user=request.user)
            return HttpResponseRedirect(newTweet.get_absolute_url())
    else:
        newTweet=Tweet.objects.create(parentTweet=tweet,text=tweet.text,user=request.user)
    return HttpResponseRedirect(tweet.get_absolute_url())
