from django.urls import path

from . import views

urlpatterns = [
    path('',views.tweets.as_view(),name="home" ),
    path('create/',views.createTweet.as_view(),name='create' ),
    path('detail/<int:pk>/',views.tweet_detail.as_view(),name='detail' ),
    path('detail/<int:id>/retweet/',views.retweet,name='retweet' ),
    path('update/<int:pk>/',views.updateTweet.as_view(),name='update' ),
    path('delete/<int:pk>/',views.deleteTweet.as_view(),name='delete' ),
]