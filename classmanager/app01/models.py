from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.
class Class(models.Model):
    title=models.CharField(max_length=32)
    ctt=models.ManyToManyField("Teacher")

class Teacher(models.Model):
    name=models.CharField(max_length=32)

class Student(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    cs=models.ForeignKey(Class,on_delete=True,related_name="test")

class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11)
    addr = models.CharField(max_length=128)


