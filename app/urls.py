
from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form'),
    path('api/students/', views.student_api, name='api'),
]
