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

class EmployeeEducation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #used to store pass , email , name 
    # PG
    CoursenamePG = models.CharField(max_length=100,null=True)
    CollegePG = models.CharField(max_length=100,null=True)
    ScorePG = models.CharField(max_length=100,null=True)
    PassoutPG = models.CharField(max_length=5,null=True)
    # G
    CoursenameG = models.CharField(max_length=100,null=True)
    CollegeG = models.CharField(max_length=100,null=True)
    ScoreG = models.CharField(max_length=100,null=True)
    PassoutG = models.CharField(max_length=5,null=True)
    # HSC
    CoursenameHSC = models.CharField(max_length=100,null=True)
    CollegeHSC = models.CharField(max_length=100,null=True)
    ScoreHSC = models.CharField(max_length=100,null=True)
    PassoutHSC = models.CharField(max_length=5,null=True)
    # SSC
    CoursenameSSC = models.CharField(max_length=100,null=True)
    CollegeSSC = models.CharField(max_length=100,null=True)
    ScoreSSC = models.CharField(max_length=100,null=True)
    PassoutSSC = models.CharField(max_length=5,null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} / {self.user.username}"

class EmployeeExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #used to store pass , email , name 
    company1name = models.CharField(max_length=100,null=True)
    company1designation = models.CharField(max_length=100,null=True)
    company1salary = models.CharField(max_length=100,null=True)
    company1duration = models.CharField(max_length=100,null=True)

    company2name = models.CharField(max_length=100,null=True)
    company2designation = models.CharField(max_length=100,null=True)
    company2salary = models.CharField(max_length=100,null=True)
    company2duration = models.CharField(max_length=100,null=True)

    company3name = models.CharField(max_length=100,null=True)
    company3designation = models.CharField(max_length=100,null=True)
    company3salary = models.CharField(max_length=100,null=True)
    company3duration = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} / {self.user.username}"
