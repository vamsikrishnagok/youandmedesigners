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

def serviceDetail(request,service_id):
   
    service = OurServices.objects.get(id=service_id)
    
    context= {
        "service":service

    }
    return render(request, 'core/service-details.html',context=context)

def projectDetail(request,work_id):
       
    service = OurWork.objects.get(id=work_id)
    
    context= {
        "service":service

    }
    return render(request, 'core/project-details.html',context=context)

def gallery(request):
    a =Gallery.objects.all()
    context = {
        "gallery":a
    }
    return render(request, 'core/gallery.html',context=context)
    

def contactUs(request):
    if request.method == "POST":
        c = Contact()        
        c.name = request.POST["name"]
        c.phone = request.POST["phone"]
        c.email = request.POST["email"]
        c.description = request.POST["message"]
        c.save()

    a = Home.objects.get(id=1)
    
    context= {
       'detail':a   

    }
    return render(request, 'core/contact.html',context=context)
