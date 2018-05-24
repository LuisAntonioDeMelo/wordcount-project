
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('Mamaefalei/', views.count,name='count'),
    path('bio/',views.bio, name='bio')
    
]
