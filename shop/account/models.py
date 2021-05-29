from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar_profile = models.ImageField('avatar profile', upload_to='account/avatars/')
    phone_number = models.CharField(max_length=12)
    address = models.TextField(blank=True)


    class Meta:
        db_table = 'account_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
