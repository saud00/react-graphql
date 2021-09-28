from django.contrib import admin
from .models import link,Employ, title, city
# Register your models here.

admin.site.register(Employ)
admin.site.register(link)
admin.site.register(title)
admin.site.register(city)