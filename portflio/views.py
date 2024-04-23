from django.http import HttpResponse
from django.shortcuts import render
# from models import slider
from service.models import  slider 
from service.models import logoimg
from service.models import myproject
from service.models import projectdetails


# from


def homepage (request):
  sliderdata=slider.objects.all()[0]
  logodata=logoimg.objects.all()[0]
  myprojectdata=myproject.objects.all()
  context ={
    'slider':sliderdata,
    'logoimg':logodata,
    'myproject':myprojectdata,
  }
  # return HttpResponse ("Hello world")
  return render(request,'index.html' ,context )


def aboutpage(request):
  # return HttpResponse ("About page")
  logodata=logoimg.objects.all()[0]
  context={
    'logoimg':logodata
  }
  return render(request,'about.html' ,context)

def crudoperations(request):
  logodata=logoimg.objects.all()[0]
  context={
    'logoimg':logodata
  }
  return render(request,'crudcrudoperations.html',context)
 



def blog(request):
  logodata=logoimg.objects.all()[0]
  context={
    'logoimg':logodata
  }
  return render(request,'blog.html',context)
  


def contactpage(request):
  logodata=logoimg.objects.all()[0]
  context={
    'logoimg':logodata
  }
  return render(request,'contact.html',context)
  


def pagenotfound(request):
  logodata=logoimg.objects.all()[0]
  context={
    'logoimg':logodata
  }
  return render(request,'pagenotfound.html',context)


def projectdetail(request,id):
  logodata=projectdetails.objects.all()[0]
  details=projectdetails.objects.filter(id=id)
  
  context={
    'logoimg':logodata,
    'projectdetails':details
    
   
  }
  return render(request,'projectdetails.html.',context )

  
