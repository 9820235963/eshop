from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    grade = models.IntegerField()
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField() 

class Product(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=25)
    price = models.FloatField()
    description = models.TextField()   

    def __str__(self):
        return self.name

      

