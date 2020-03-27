from django.contrib import admin
from .models import Account
# Register your models here.

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('accountName','accountNumber','accountType','accountBalance','customer_id','currency_id')
    search_fields = ('accountName','accountNumber')

admin.site.register(Account,AccountsAdmin)
