from django.urls import path

from . import views,accesscontrol

urlpatterns = [
    path('addtask/', views.addTask, name='addTask'),
    path('gettask/', views.getTask, name='getTask'), 
    path('signup/',accesscontrol.sign_up,name='sign_up'),
    path('signin/',accesscontrol.sign_in,name='sign_in'),
    
]