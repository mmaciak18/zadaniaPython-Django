from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randrange

class User(AbstractUser):
    username = models.CharField(unique=True, null=True, blank=False, max_length=128)
    password = models.CharField(null=True, blank=False, max_length=128)
    birth_date = models.DateField(null=True, blank=False)
    rand = models.IntegerField(null=False, blank=False, default=randrange(1, 100))

    USERNAME_FIELD = 'username'
