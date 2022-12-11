

# Create your models here.
from django.db import models

# Create your models here.
class employment(models.Model):
    designation =models.CharField(max_length=100)
    description =models.CharField(max_length=100)
    duration =models.IntegerField()
    
    notice_period_days=models.IntegerField()

    
class skills(models.Model):

     skill_name =models.CharField(max_length=150)
     experience_years=models.IntegerField()

class edu(models.Model):
    program=models.CharField(max_length=100) 
    University_name=models.CharField(max_length=200) 
    date_passed=models.DateField()
    course_duration=models.IntegerField()

class personal(models.Model):
    name=models.CharField(max_length=30) 
    email_id=models.CharField(max_length=50) 
    phone=models.BigIntegerField() 
    address=models.CharField(max_length=500)
