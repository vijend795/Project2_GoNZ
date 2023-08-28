from django.contrib import admin
from django.urls import path
from .views import SignUpView,user_profile

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    # path('profile/',UserProfile.as_view(),name='profile'),
    path('profile/',user_profile, name='profile'),

    
   
]
