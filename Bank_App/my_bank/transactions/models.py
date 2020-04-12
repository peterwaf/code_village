from django.db import models


# Create your models here.

class Transactions(models.Model):
    date = models.DateTimeField(auto_now=True)
    cashIn = models.FloatField()
    cashOut = models.FloatField()
    transactionFee = models.FloatField()
    balance = models.FloatField()
    customer = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'tbl_name_transactions'
    
    def __str__(self):
        return self.customer