from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('our-work/', views.ourWork, name='ourWork'),
    path('our-services/', views.ourServices, name='ourServices'),
    path('gallery/', views.gallery, name='gallery'),
    
]