from django.contrib import admin

from device.models import Marques, Category, Appareils

# Register your models here.
admin.site.register(Marques)
admin.site.register(Category)
admin.site.register(Appareils)