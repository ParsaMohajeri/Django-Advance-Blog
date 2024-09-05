from django.db import models
from django.coontrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
# Create your models here.

class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)

    USERNAME_FIELD ='email'
    REQUIRED_FIELD =[]
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)





    def __str__(self):
        return self.email


