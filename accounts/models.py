from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations=True

    def _create_user(self,username,password,**extra_fields):
        if not username:
            raise ValueError("username required")

        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self,username,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)

        return self._create_user(username,password,**extra_fields)

    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser is_staff must be True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("superuser is_superuser must be True")

        
        return self._create_user(username,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):

  
    first_name=models.CharField('first name',max_length=100,blank=True)
    last_name=models.CharField('last name',max_length=100,blank=True)
    username = models.CharField(unique=True, max_length=255, blank=False)
    email = models.EmailField(unique=True,max_length=300)
    department = models.CharField(max_length=100,default=None,null=True)
    catagory = models.CharField(max_length=100, default=None,null=True)
    is_staff=models.BooleanField('staff status',default=False)
    is_active=models.BooleanField('active',default=False)
    is_superuser=models.BooleanField('super user',default=False)
    #date_joined = models.DateTimeField('date joined', default=timezone.now())
    

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username

    def full_name(self):
        return self.first_name+" "+self.last_name




