
from django.urls import path,include
from . import views
 
app_name="tags"
urlpatterns = [
    path('tag/<str:tag>', views.visitTag,name='tag'),
]
