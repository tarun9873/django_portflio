from django.http import HttpResponse
from django.shortcuts import render
# from models import slider
from service.models import  slider 
from service.models import myproject
from service.models import projectdetails


# from


def homepage (request):
  sliderdata=slider.objects.all()[0]
  # logodata=logoimg.objects.all()[0]
  myprojectdata=myproject.objects.all()
  context ={
    'slider':sliderdata,
    # 'logoimg':logodata,
    'myproject':myprojectdata,
  }
  # return HttpResponse ("Hello world")
  return render(request,'index.html' ,context )


def aboutpage(request):
  # return HttpResponse ("About page")

  return render(request,'about.html' )

def crudoperations(request):

  
  return render(request,'crudcrudoperations.html')
 



def blog(request):

 
  return render(request,'blog.html')
  


def contactpage(request):

 
  return render(request,'contact.html')
  


def pagenotfound(request):


  return render(request,'pagenotfound.html')


def projectdetail(request,id):
  details=projectdetails.objects.filter(id=id)
  
  context={
    'projectdetails':details
    
   
  }
  return render(request,'projectdetails.html.',context )

  
