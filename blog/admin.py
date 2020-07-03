from django.contrib import admin
from .models import Blog

admin.site.register(Blog)       #creates blog model in admin page, can be accessed by superuser
