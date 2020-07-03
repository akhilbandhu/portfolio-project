from django.contrib import admin

from .models import Job

admin.site.register(Job)        #creates job model in admin page, can be accessed by superuser directly
