from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django.contrib import auth, messages
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from datetime import datetime

from services.models import UserNotifications, DirectorPenRequest, OfficerPenRequest, ProcessedRequest, Inventory

from services.generate_id import generate_id


# Create your views here.

User = get_user_model()

def home(request):

    your_notifications = None

    """UserNotifications.objects.all().delete()
    OfficerPenRequest.objects.all().delete()
    DirectorPenRequest.objects.all().delete()
    ProcessedRequest.objects.all().delete()"""
    #Inventory.objects.all().delete()

    if request.user.is_authenticated:
        your_notifications = UserNotifications.objects.filter(username = request.user.username)
        #print(generate_id())
        return render(request,'home.html', {'your_notifications':your_notifications,
                                            'length':len(your_notifications),'catagory':request.user.catagory})

    else:
        return render(request,'home.html')
    
def contact(request):
    return render(request,'contact_us.html')

def about(request):
    return render(request,'about.html')


def user_login(request):

    if request.method == 'GET':
        return render(request,'accounts/login.html')

    else:
        form_username=request.POST['username']
        form_password=request.POST['password']

        user = auth.authenticate(request,username=form_username,password=form_password)

        
        if user is not None:
            auth.login(request,user)
            messages.info(request,message="login successful")
            return redirect('/')

        else:
            if not User.objects.filter(username=form_username).exists():
                messages.info(request,message="username doesn't exist")
                return redirect('/auth/login')
            
            else:
                messages.info(request,message="incorrect password")
                return redirect('/auth/login')

def user_logout(request):
    auth.logout(request)
    messages.info(request,message="logout successful")
    return redirect('/')

def change_pw(request):
    if request.method == "GET":
        return render(request,'accounts/change_pw.html')

    else:
        form_current_pw = request.POST['current_pw']
        form_password1 = request.POST['password1']
        form_password2 = request.POST['password2']

        correct_pw = check_password(form_current_pw, request.user.password)
        #request.user.set_password(form_current_pw)
        print(correct_pw)

        if not correct_pw:
            messages.info(request,message= "incorrect current password, login again")
            auth.logout(request)
            return redirect('/auth/login')

        else:

            if form_password1 != form_password2:
                messages.info(request,message="new passwords don't match")
                return redirect('/auth/login/change_pw')

            else:
                request.user.set_password(form_password1)
                request.user.save()
                auth.login(request,request.user)
                messages.info(request,message="password changed succesfully")
                return redirect('/')






