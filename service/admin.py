from django.contrib import admin
from .models import slider
from .models import myproject
from .models import projectdetails



class myprojectadmin(admin.ModelAdmin):
  list_display=['image_tag','title' ,'description_title','add_date']
  search_fields=['title','description_title',]

# Register your models here.
admin.site.register(myproject , myprojectadmin)





class projectdetailsadmin(admin.ModelAdmin):
  list_display=['image_tag','project_name','post_title','description','add_date']
  search_fields=['post_title',]

admin.site.register(projectdetails,projectdetailsadmin)



class slideradmin(admin.ModelAdmin):
  list_display=['image_tag','title','title_short','title_long','pdf']

admin.site.register(slider,slideradmin)





