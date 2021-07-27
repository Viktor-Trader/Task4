from django.urls import path
from . import views

urlpatterns = [
    path('', views.front),
    path('about', views.about),
    path('registration', views.registration)
]