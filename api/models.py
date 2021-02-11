from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    created_at = models.DateField(auto_now_add=True)
    task_finish = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
