from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=40, verbose_name='телефон', null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

