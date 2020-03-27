from django.db import models
from customer.models import Customer
# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=100)
    currencyname = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tbl_currency'
    
    def __str__(self):
        return self.code