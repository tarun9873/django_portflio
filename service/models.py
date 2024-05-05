# Create your models here.
from django.db import models
from django.utils.html import format_html


# Create your models here.

class hear_me(models.Model):
  full_name=models.CharField(max_length=100)
  email=models.EmailField(max_length=100)
  number=models.CharField(max_length=20)
  message=models.TextField(max_length=100)

  def __str__(self):
        return self.full_name

class slider (models.Model):
  title =models.CharField(max_length=100 ,blank=False)
  title_short =models.CharField(max_length=500 ,blank=False)
  title_long =models.TextField(max_length=1000 ,blank=False)
  image =models.ImageField(upload_to='slider',blank=False)
  pdf =models.FileField(upload_to='slider',blank=False)
  
  

  def __str__(self):
    return self.title
  def image_tag(self):
    return format_html('<img src="/Media_upload/{}"  style="width: 60px; height: 100px;border: 4px solid red;" />'.format(self.image))
  
  
#  logo titile top logo 

  

  # my project 

class myproject (models.Model):
  description_title =models.CharField(max_length=100 ,blank=False)
  title =models.CharField(max_length=100 ,blank=False)
  add_date=models.DateTimeField(null=True,auto_now_add=True)
  project_image =models.ImageField(upload_to='project_image',blank=False)
  # urlLink =models.URLField(blank=False ,null=True)

  def __str__(self):
    return self.title
  def image_tag(self):
    return format_html('<img src="/Media_upload/{}"  style="width: 60px; height: 50px;border: 4px solid red;" />'.format(self.project_image))

  


class projectdetails (models.Model):
  project_name =models.ForeignKey(myproject,on_delete=models.CASCADE)
  post_title =models.CharField(max_length=100 ,blank=False)
  description =models.TextField(max_length=1000 ,blank=False)
  project_image =models.ImageField(upload_to='projectdetails',blank=False)
  add_date=models.DateTimeField(auto_now_add=True,null=True)
  Url_add=models.URLField(null=True, blank=True)


  def image_tag(self):
    return format_html('<img src="/Media_upload/{}"  style="width: 60px; height: 50px;border: 4px solid red;" />'.format(self.project_image))

  def __str__(self):
    return self.post_title   


    





  