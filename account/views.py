from django.shortcuts import render,get_object_or_404,reverse,HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.http import JsonResponse
from account.common.decorators import ajax_required
from django.views.decorators.http import require_POST
# Create your views here.

class userProfile(DetailView):
    model = User
    template_name = "tweets/profile.html"
    def get_object(self):
        return User.objects.get(username=self.kwargs['username'])


def following(request,id):
    print('ok')
    user_id=id
    user=get_object_or_404(User,id=user_id)
    if user in request.user.followings.all():
        print('followed')
        request.user.profile.followings.add(user)
    else:
        print('unfollowd')
        request.user.profile.followings.remove(user)

    return HttpResponseRedirect(reverse("profile",kwargs={'username':user.username}))

def new_method(request,id):
    user=get_object_or_404(User,id=request.POST['id'])
    action=request.POST['action']
    if action == 'follow':
        request.user.profile.followings.add(user)
    else:
        request.user.profile.followings.remove(user)
    print('ajax_func')
    return JsonResponse(data={'status':'ok'})



