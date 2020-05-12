from rest_framework import serializers
from account.api.serializers import userSerializer
from django.utils.timesince import timesince
from tweet.models import Tweet


class TweetModelSerializer(serializers.ModelSerializer):
    user = userSerializer(read_only=True)
    time_display =serializers.SerializerMethodField()
    time_since = serializers.SerializerMethodField()
    class Meta:
        model=Tweet
        fields=['user','text','created','time_display','time_since']

    def get_time_display(self,obj):
        return obj.created.strftime("%b %d %Y %H:%M:%S")

    def get_time_since(self,obj):
        return timesince(obj.created)+" "+"ago"