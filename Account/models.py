from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Account(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    login_count = models.IntegerField(default=1)
    Timestamps = models.DateTimeField(default=datetime.datetime.now, verbose_name='Timestamps')

    USERNAME_FIELD = 'username'

    objects = BaseUserManager()

