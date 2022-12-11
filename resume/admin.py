from django.contrib import admin

# Register your models here.
from resume.models import employment
from resume.models import skills
from resume.models import edu
from resume.models import personal

class empAdmin(admin.ModelAdmin):
   pass

admin.site.register(employment,empAdmin)

class skillAdmin(admin.ModelAdmin):
   pass
admin.site.register(skills,skillAdmin)

class eduAdmin(admin.ModelAdmin):
   pass
admin.site.register(edu,eduAdmin)

class personalAdmin(admin.ModelAdmin):
   pass
admin.site.register(personal,personalAdmin)


