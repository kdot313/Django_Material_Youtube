from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)

class Products(models.Model):
    pass