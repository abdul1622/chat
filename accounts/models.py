from email import message
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your models here.
# class MyUserManager(BaseUserManager):
#     def create_user(self,email,phone):
#         if not email:
#             raise ValueError('give ur email')
#         if not phone:
#             raise ValueError('give ur phone')
#         user = self.model(email=self.normalize_email(email))
#         user.phone = phone
#         user.save(using=self.db)
#         return user

#     def create_superuser(self,email,phone):
#         user = self.create_user(email=email,phone=phone)
#         user.is_admin_user = True
#         user.save(using=self.db)
#         return user

# class User(AbstractBaseUser):
#     email = models.EmailField(unique = True)
#     phone = models.TextField(unique = True,  validators=[
#             MinLengthValidator(10),
#             MaxLengthValidator(10)
#         ])
#     is_admin_user = models.BooleanField(default= False)
#     created_at = models.DateTimeField(default=timezone.now)
#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone']


#     def __str__(self):
#         return self.email

#     def has_perm(self,perm,obj=None):
#         return True

#     def has_module_perm(self,app_label):
#         return True

#     @property
#     def is_admin(self):
#         return self.is_admin == True



class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='person')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='friend')
    note = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note
