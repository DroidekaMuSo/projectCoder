from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=40)
    generation = models.IntegerField(unique=True)

    def __str__(self):
        return f'Course: {self.name}, Generation: {self.generation}'


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'''
        Name: {self.name}
        Last name: {self.last_name}
        Email: {self.email} '''


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    job = models.CharField(max_length=30)

    def __str__(self):
        return f'''
          Name: {self.name}
          Last name: {self.last_name}
          Email: {self.email} 
          Job: {self.job}'''


class Homework(models.Model):
    name = models.CharField(max_length=30)
    sub_date = models.DateField()
    sub = models.BooleanField()

