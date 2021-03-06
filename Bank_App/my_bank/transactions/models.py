from django.db import models
from customer.models import Customer

# Create your models here.

class Transactions(models.Model):
    date = models.DateTimeField(auto_now=True)
    cashIn = models.CharField(max_length=200)
    cashOut = models.CharField(max_length=200)
    transactionFee = models.FloatField()
    balance = models.FloatField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbl_name_transactions'
    
    def __str__(self):
        return self.customer