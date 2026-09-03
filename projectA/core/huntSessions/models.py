from django.db import models

# Create your models here.


class Hunt(models.Model):
    hunt_Id = models.AutoField(primary_key=True)
    hunt_Name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

'''
class Question(models.Model):
    Question_Id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000)
    Question_type = models.CharField(max_length=50)
    answer = models.CharField(max_length=250)
'''