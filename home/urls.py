from django.contrib import admin
from django.urls import path, include
from .import views
app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('portfolio', views.portfolio_view, name='portfolio'),
    path('price', views.price_view, name='price'),
    path('services', views.services_view, name='services'),
    path('contact', views.contact_view, name='contact'),
]
