from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

#class to create a custom user

class CustomUserAdmin(BaseUserAdmin):
    #lists to display
    list_display = ('email','username','first_name','last_name','mobile_number','pin','is_active','is_staff')
    #fields to search in the admin
    search_fields = ('email','username','mobile_number')
    list_filter = ('date_joined',)
    #if you want extended fields to be edited in the admin, add field sets
    fieldsets = (
    (None, {'fields': ('username', 'password','pin')}),
    ('Personal info', {'fields': ('first_name','last_name','email','mobile_number')}),
    ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
)

#register in the admin

admin.site.register(CustomUser,CustomUserAdmin)