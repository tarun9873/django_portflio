# Create your models here.
from django.db import models

# Create your models here.




class slider (models.Model):
  title =models.CharField(max_length=100 ,blank=False)
  title_short =models.CharField(max_length=500 ,blank=False)
  title_long =models.TextField(max_length=1000 ,blank=False)
  image =models.ImageField(upload_to='slider',blank=False)
  pdf =models.FileField(upload_to='slider',blank=False)
  
  

  def __str__(self):
      return self.title
  
  
#  logo titile top logo 

class logoimg (models.Model):
  title =models.CharField(max_length=100 ,blank=False)
  logo =models.ImageField(upload_to='logo',blank=False)
  toplogo =models.ImageField(upload_to='logo',blank=False)


  def __str__(self):
      return self.title
  

  # my project 

class myproject (models.Model):
  description_title =models.CharField(max_length=100 ,blank=False)
  title =models.CharField(max_length=100 ,blank=False)
  project_image =models.ImageField(upload_to='project_image',blank=False)

  def __str__(self):
    return self.title
  


class projectdetails (models.Model):
  project_name =models.ForeignKey(myproject,on_delete=models.CASCADE)
  post_title =models.CharField(max_length=100 ,blank=False)
  description =models.TextField(max_length=1000 ,blank=False)
  project_image =models.ImageField(upload_to='projectdetails',blank=False)

  def __str__(self):
    return self.post_title   


    





  