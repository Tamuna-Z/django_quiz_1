from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stack/', views.stack, name='stack'),
    path('teamleads/', views.teamleads, name='teamleads'),
    path('employee/', views.employee, name='employee')
]
