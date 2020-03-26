from django.db import models
from customer.models import Customer
from currency.models import Currency
# Create your models here.
class Account(models.Model):
    accountName = models.CharField(max_length=100)
    accountNumber = models.IntegerField()
    accountType = models.CharField(max_length=100)
    accountBalance = models.IntegerField()
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    currency_id = models.ForeignKey(Currency,on_delete=models.CASCADE,default=1)
    
    class Meta:
        db_table = 'tbl_accounts'