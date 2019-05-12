from django.db import models

# Create your models here.


class Home(models.Model):
    banner_image = models.ImageField(blank=True,null=True)
    banner_area_text = models.TextField(blank=True,null=True)
    logo = models.ImageField(blank=True,null=True)
    services_title = models.CharField(max_length=100,blank=True,null=True)
    services_description = models.CharField(max_length=200,blank=True,null=True)
    services_desc_large = models.TextField(blank=True,null=True)
    work_title = models.CharField(max_length=100,blank=True,null=True)
    work_description = models.CharField(max_length=200,blank=True,null=True)
    work_desc_large = models.TextField(blank=True,null=True)
    our_address = models.CharField(max_length=500,blank=True,null=True)
    our_phone =  models.CharField(max_length=500,blank=True,null=True)
    our_mail = models.CharField(max_length=500,blank=True,null=True)
    about_us = models.TextField(blank=True,null=True)



class OurServices(models.Model):
    img = models.ImageField(blank=True,null=True)
    heading = models.CharField(max_length=20)
    short_content = models.CharField(max_length=150)
    content = models.TextField()

class OurWork(models.Model):
    img = models.ImageField(blank=True,null=True)
    ratings = models.IntegerField(blank=True,null=True)
    client = models.CharField(max_length=100,blank=True,null=True)
    client_website = models.CharField(max_length=100,blank=True,null=True)
    completed = models.DateTimeField(blank=True,null=True)
    title = models.CharField(max_length=20)
    short_content = models.CharField(max_length=150)
    content = models.TextField()

class Gallery(models.Model):
    image = models.ImageField()

class Contact(models.Model):
    name = models.CharField(max_length=500,blank=True,null=True)
    phone = models.CharField(max_length=500,blank=True,null=True)
    email = models.CharField(max_length=500,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)

class Blog(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    short_desc = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField()
    published_date = models.DateTimeField()
    viewss = models.IntegerField(default=0)
    image = models.ImageField()






