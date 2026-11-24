from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_directory, name='directory'),
    path('register/', views.register_student, name='register'),
]
