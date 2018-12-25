from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharFiled(max_length=128)
    last_name = models.CharFiled(max_length=128)
    email = models.EmailFiled(max_length=264,unique=True)
