from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User
from a1.models import info,Donation

# Register your models here.
admin.site.register(info)

admin.site.register(Donation)

class CustomerUserAdmin(UserAdmin):
    admin.site.unregister(User)

admin.site.register(User,CustomerUserAdmin)