from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    idNumber = models.IntegerField()
    uniqueID = models.IntegerField()
    mobileNo = models.CharField(max_length=12)
    pin = models.CharField(max_length=5)
    
    class Meta:
        db_table = 'tbl_customers'
    
    def __str__(self):
        return self.name