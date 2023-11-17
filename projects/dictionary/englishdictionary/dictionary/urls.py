
from django.urls import path
from .views import wordview,index



urlpatterns= [
    path('',index,name='index'),
    path('word/',wordview,name='word')

]