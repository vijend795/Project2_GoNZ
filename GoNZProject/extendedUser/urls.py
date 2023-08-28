from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('agents/', views.users_list, name='users-list'),
    path('agent/<int:agent_id>/', views.user_details, name='user-details'),

]
