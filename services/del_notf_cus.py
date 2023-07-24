from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth, messages

from .models import UserNotifications

User = get_user_model()

def del_notf_cus(request, notification_id):
    UserNotifications.objects.filter(cus_id = notification_id).delete()
    messages.info(request,message='Notification deleted')
    return redirect('/')