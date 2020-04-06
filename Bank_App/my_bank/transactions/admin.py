from django.contrib import admin
from .models import Transactions
# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date','cashIn','cashOut','transactionFee','balance','customer')
    search_fields = ('date','customer')
admin.site.register(Transactions,TransactionAdmin)