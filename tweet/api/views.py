from rest_framework import generics
from rest_framework import permissions
from .serializers import TweetModelSerializer
from tweet.models import Tweet
from django.contrib.auth.models import User
from account.models import profile

class ListTweetApi(generics.ListAPIView):
    serializer_class=TweetModelSerializer
    def get_queryset(self):
        qs = Tweet.objects.all().order_by('-created')
        query=self.request.GET.get('q',None)
        if query:
            qs=qs.filter(text__icontains=query)
        return qs

class ListFollowTweetApi(generics.ListAPIView):
    print('cool')
    serializer_class=TweetModelSerializer
    print()
    def get_queryset(self):
        # hany=User.objects.first()
        all_follow=self.request.user.profile.followings.values_list('id',flat=True)
        qs1 = Tweet.objects.filter(user_id__in=all_follow)
        qs2=Tweet.objects.filter(user=self.request.user)
        qs=(q1|q2).distinct().order_by('-created')
        query=self.request.GET.get('q',None)
        if query:
            qs=qs.filter(text__icontains=query)
        return qs


class createTweetApi(generics.CreateAPIView):
    serializer_class=TweetModelSerializer
    permissionclasses=[permissions.IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)




         