from django.urls import path
from . import views

app_name = 'fb_profile'

urlpatterns = [
    path('', views.profile_view, name='profile'),
]
