from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, username, first_name, last_name, email, password):
        if username is None:
            raise TypeError('Usuário deve ter username')
        if username is None:
                raise TypeError('Usuário deve ter email')

        user = self.model(username=username, emial=self.normalize_email(email), first_name=first_name, last_name = last_name)
        user.set_password(password)
        user.is_superuser = False
        user.is_staff = False
        user.save()





class Task(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    created_at = models.DateField(auto_now_add=True)
    task_finish = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
