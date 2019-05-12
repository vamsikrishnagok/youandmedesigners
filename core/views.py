from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, reverse
from core.models import Home,OurServices,OurWork,Contact,Blog,Gallery
# Create your views here.


def home(request):
    a = Home.objects.get(id=1)
    services = OurServices.objects.all()[:3]
    projects = OurWork.objects.all()[:8] 
    blogs = Blog.objects.all()[:3]  

    context= {
        "home_banner":a.banner_area_text,
        "services_title":a.services_title,
        "services_description":a.services_description,
        "work_title":a.work_title,
        "work_description":a.work_description,
        "services":services,
        "projects":projects,
        "blogs":blogs       

    }
    return render(request, 'core/index.html',context=context)


def about(request):
    a = Home.objects.get(id=1)
    projects = OurWork.objects.all()[:8] 
    context = {
        "about_us":a.about_us,
        "work_title":a.work_title,
        "work_description":a.work_description,
        "projects":projects,

    }
    return render(request, 'core/about-us.html',context=context)


def ourWork(request):
    a = Home.objects.get(id=1)
    projects = OurWork.objects.all()[:8] 
    context = {
        "about_us":a.about_us,
        "work_title":a.work_title,
        "work_description":a.work_description,
        "projects":projects,

    }
    return render(request, 'core/projects.html',context=context)


def ourServices(request):
    a = Home.objects.get(id=1)
    services = OurServices.objects.all()
    projects = OurWork.objects.all()[:8] 
    context= {
        "services_title":a.services_title,
        "services_description":a.services_description,
        "work_title":a.work_title,
        "work_description":a.work_description,
        "projects":projects,        
        "services_title":a.services_title,
        "services_description":a.services_description,       
        "services":services,
           

    }
    return render(request, 'core/services.html',context=context)

def gallery(request):
    a =Gallery.objects.all()
    context = {
        "gallery":a
    }
    return render(request, 'core/gallery.html',context=context)