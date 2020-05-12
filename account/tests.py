from django.test import TestCase
from .models import profile
from django.contrib.auth.models import User
# Create your tests here.


class testProfile(TestCase):
    
    def setUp(self):
        self.username="some"
        User.objects.create(username=self.username)

    def checkProfile(self):
        print('tested')
        self.assertTrue(profile.objects.filter(user_username=self.username).exists())
        print(profile.objects.last())