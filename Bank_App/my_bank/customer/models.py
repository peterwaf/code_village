from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    idNumber = models.IntegerField()
    uniqueID = models.IntegerField()
    mobileNo = models.IntegerField()
    pin = models.IntegerField()
    
    class Meta:
        db_table = 'tbl_customers'