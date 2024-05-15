from django.contrib import admin
from .models import slider
from .models import myproject
from .models import projectdetails
from .models import hear_me
from .models import contact



class myprojectadmin(admin.ModelAdmin):
  list_display=['image_tag','title' ,'description_title','add_date']
  search_fields=['title','description_title',]

# Register your models here.
admin.site.register(myproject , myprojectadmin)





class projectdetailsadmin(admin.ModelAdmin):
  list_display=['image_tag','project_name','post_title','Url_add','description','add_date']
  search_fields=['post_title',]

admin.site.register(projectdetails,projectdetailsadmin)



class slideradmin(admin.ModelAdmin):
  list_display=['image_tag','title','title_short','title_long','pdf']

admin.site.register(slider,slideradmin)



class hear_meadmin(admin.ModelAdmin):
  list_display=['full_name','email','number','message','add_date']
admin.site.register(hear_me,hear_meadmin)



class contact_admin(admin.ModelAdmin):
  list_display=['full_name','email','number','msg','add_date']
admin.site.register(contact,contact_admin)





