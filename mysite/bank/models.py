from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=8)
    balance = models.IntegerField(default=0)
