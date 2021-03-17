from django.db import models

# Create your models here.
class Signup(models.Model):
    email=models.EmailField()
    username=models.TextField(max_length=30)
    password=models.TextField(max_length=20)
    