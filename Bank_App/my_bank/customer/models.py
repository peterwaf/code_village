from django.db import models
from user.models import CustomUser
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    idNumber = models.IntegerField()
    uniqueID = models.IntegerField()
    mobileNo = models.CharField(max_length=12)
    pin = models.CharField(max_length=5)
    user = models.ForeignKey(CustomUser,default=1,null=False,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbl_customers'
    
    def __str__(self):
        return self.name