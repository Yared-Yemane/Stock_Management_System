from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.postgres.fields import ArrayField



# Create your models here.

User = get_user_model()

class Inventory(models.Model):
    item_name = models.CharField(max_length=100, default=None)
    item_amount = models.PositiveIntegerField(default=0)
    cus_id = models.CharField(max_length=100,default='unassigned')

    def __str__(self):
        return self.item_name

class DirectorPenRequest(models.Model):
    cus_id=models.CharField(max_length=100,default='unassigned')
    item_name = models.CharField(max_length=100, default=None)
    item_amount = models.IntegerField(default=1)
    #request_dateTime = models.DateTimeField(default=datetime.now())
    username = models.CharField(max_length=100,default=None)
    first_name = models.CharField(max_length=100,default=None)
    last_name = models.CharField(max_length=100, default=None)
    user_department = models.CharField(max_length=100,default=None)
    user_duty = models.CharField(max_length=100,default=None)
    director_fullname = models.CharField(max_length=200, default='`unassigned`')
    #officer_fullname = models.CharField(max_length=200, default='unassigned')
    approval =  models.CharField(max_length=10,default='unassigned')
    user_description = models.TextField(max_length=1000,default='unassigned')

    """def get_absolute_url(self):
        return reverse_lazy('process_request',kwargs={'item_request_id':self.id})

    pass"""

    def __str__(self):
        return self.first_name

class OfficerPenRequest(models.Model):
    cus_id=models.CharField(max_length=100,default='unassigned')
    item_name = models.CharField(max_length=100, default=None)
    item_amount = models.IntegerField(default=1)
    #request_dateTime = models.DateTimeField(default=datetime.now())
    first_name = models.CharField(max_length=100,default=None)
    last_name = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100,default=None)
    user_department = models.CharField(max_length=100,default=None)
    user_duty = models.CharField(max_length=100,default=None)
    officer_fullname = models.CharField(max_length=200, default='unassigned')
    approval =  models.CharField(max_length=10,default='rejected')
    notified = models.BooleanField(default=False)
    director_description = models.TextField(max_length=1000,default='unassigned')
    user_description = models.TextField(max_length=1000,default='unassigned')


    """def get_absolute_url(self):
        return reverse_lazy('process_request',kwargs={'item_request_id':self.id})
"""

class UserNotifications(models.Model):
    username = models.CharField(max_length=100, default='unassigned')
    message = models.CharField(max_length=200, default='unassigned')
    cus_id=models.CharField(max_length=100,default='unassigned')
    additional_info = ArrayField(models.CharField(max_length=100,default='unassigned'),default=list)

    def db_type(self, connection):
        return 'array'
  

    def __str__(self):
        return self.message

class ProcessedRequest(models.Model):
    cus_id=models.CharField(max_length=100,default='unassigned')
    item_name = models.CharField(max_length=100, default=None)
    item_amount = models.IntegerField(default=1)
    #request_dateTime = models.DateTimeField(default=datetime.now())
    first_name = models.CharField(max_length=100,default=None)
    last_name = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100,default=None)
    user_department = models.CharField(max_length=100,default=None)
    user_duty = models.CharField(max_length=100,default=None)
    officer_fullname = models.CharField(max_length=200, default="unassigned")
    approval =  models.CharField(max_length=10,default='unassigned')
    officer_description = models.TextField(max_length=1000,default='unassigned')
    director_description = models.TextField(max_length=1000,default='unassigned')
    user_description = models.TextField(max_length=1000,default='unassigned')


    def __str__(self):
        return self.item_name


    """def get_absolute_url(self):
        return reverse_lazy('process_request',kwargs={'item_request_id':self.id})"""    