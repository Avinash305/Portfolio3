from django.contrib import admin
from .models import *
# Register your models here.

class Admincontact_details(admin.ModelAdmin):
    list_display = ['name','email','mobile','message']


admin.site.register(contact_details,Admincontact_details)