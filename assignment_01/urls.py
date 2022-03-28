from django.urls import path
from . import views

urlpatterns = [
    path('', views.python, name="python"),
    path('assignment1', views.ass1_home, name="ass1-home"),
    path('fixed/', views.fixed, name="fixed"),
    path('range/', views.myRange, name="range"),
    path('random/', views.random, name="random"),
]