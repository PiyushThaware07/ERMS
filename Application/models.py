from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #used to store pass , email , name 
    emp_id = models.CharField(max_length=50)
    department = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=50,null=True)
    joiningDate = models.DateField(null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} / {self.user.username}"