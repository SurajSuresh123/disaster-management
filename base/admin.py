from django.contrib import admin

# Register your models here.
from .models import CitizenUser,StaffUser
admin.site.register(CitizenUser)
admin.site.register(StaffUser)