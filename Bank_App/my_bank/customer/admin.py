from django.contrib import admin
from.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','idNumber','mobileNo','pin') #list_display is inbuilt
    search_fields = ('name','idNumber') #seach fields is inbuilt
    
#allow display multiple items on admin page
admin.site.register(Customer,CustomerAdmin)