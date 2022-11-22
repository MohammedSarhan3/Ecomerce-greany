from django.contrib import admin
from .models import Profile,UserPhoneNumber, UserAdress
# Register your models here.
admin.site.register(Profile)
admin.site.register(UserPhoneNumber)
admin.site.register(UserAdress)