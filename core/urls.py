from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('our-work/', views.ourWork, name='ourWork'),
    path('our-services/', views.ourServices, name='ourServices'),
    path('<int:service_id>/service/', views.serviceDetail, name='serviceDetail'),
    path('<int:work_id>/project/', views.projectDetail, name='projectDetail'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contactUs, name='contactUs'),
    
]