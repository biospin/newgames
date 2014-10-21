from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.CharField(max_length=30)
    month  = models.IntegerField()
