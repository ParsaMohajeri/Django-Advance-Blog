from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    """
    custome user model manager where email is the unique identifier for
    authentication instead of usernames.
    """
    def create_user(self, email, password,**extra_fields):
        """
        create and save a User with the given email and password
        and or extra data
        """
        if not email:
            raise ValueError(_("the email must be set"))
        email= self.normalize_email(email)
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        


    def create_superuser(self,email,password,**extra_fields):
        """
        create and save a User with the given email and password
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)


        if extra_fields.get ('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get ('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))     

        return self.create_user(email,password,**extra_fields)
        



class User (AbstractBaseUser, PermissionsMixin):
    """
    custome User model for our app
    """
    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)

    USERNAME_FIELD ='email'
    REQUIRED_FIELD =[]
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    objects = UserManager()



    def __str__(self):
        return self.email


class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    image=models.ImageField(blank=True,null=True)
    description=models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)



    def __str__ (self):
        self.user.email
