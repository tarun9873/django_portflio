from django.http import HttpResponse
from django.shortcuts import render
# from models import slider
from service.models import  slider 
from service.models import myproject
from service.models import projectdetails
from service.models import hear_me


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

  if request.method=="POST":
    name=request.POST['full_name']
    email=request.POST['email']
    number=request.POST['number']
    message=request.POST['message']
    
    # print(name ,email,number,message)
    data=hear_me(full_name=name,email=email,number=number,message=message)
    data.save()


  return render(request,'index.html' ,context )


def aboutpage(request):
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
  alldetails=projectdetails.objects.filter(project_name_id =id)
  
  context={
    'projectdetails':alldetails
  }
  return render(request,'projectdetails.html.',context )

  
