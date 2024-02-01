from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('contactus', views.contact,name='contactus'),
    path('customer_services', views.customer_services,name='customer_services'),
]