from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    SADMIN = 'sadmin'
    ROLES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
        (SADMIN, 'sadmin'),
    )
    bio = models.TextField(max_length=500, blank=True, null=True)
    role = models.CharField(max_length=30, choices=ROLES, default='user')
    confirmation_code = models.CharField(max_length=200, default='FOOBAR')
