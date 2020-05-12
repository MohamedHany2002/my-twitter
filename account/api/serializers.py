from django.contrib.auth.models import User
from rest_framework import serializers
from django.urls import reverse


class userSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    profile_url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name','follower_count','profile_url']

    def get_follower_count(self,obj):
        print(obj.username)
        return 0

    def get_profile_url(self,obj):
        return reverse("profile",kwargs={'username':obj.username})
        
