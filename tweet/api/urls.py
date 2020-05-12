
from django.urls import path,include
from . import views
 

urlpatterns = [
    path('', views.ListTweetApi.as_view()),
    path('home/', views.ListFollowTweetApi.as_view(),name='tweets_home'),
    path('create/', views.createTweetApi.as_view()),
]
