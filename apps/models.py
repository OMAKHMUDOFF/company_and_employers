from django.db import models

# Create your models here.
class Company(models.Model):
  name = models.CharField(max_length = 255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  
  class Meta: 
    verbose_name_plural = 'Companies'
  
  
  def __str__(self) -> str:
    return self.name
  
class Employer(models.Model):
  name = models.CharField(max_length=255)
  company = models.ForeignKey(Company, on_delete = models.CASCADE)
  position = models.CharField(max_length=255)
  salary = models.IntegerField(default = 0)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  
  def __str__(self) -> str:
    return self.name
  

class Employee(models.Model):
  name = models.CharField(max_length=255)
  company = models.ForeignKey(Company, on_delete = models.CASCADE)
  employer = models.ForeignKey(Employer, on_delete = models.DO_NOTHING)
  position = models.CharField(max_length=255)
  salary = models.IntegerField(default = 0)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  
  def __str__(self) -> str:
    return self.name