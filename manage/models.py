from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    date_of_birth = models.TextField()
    grade = models.IntegerField()
    phone = models.TextField()
    email = models.TextField()

    