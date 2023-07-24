from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth, messages

User = get_user_model()

def add_user_cus(request):
    
    if request.method == 'GET':
        return render(request,'services/add_user.html')

    else:
        form_first_name=request.POST['first_name']
        form_last_name=request.POST['last_name']
        form_user_name=request.POST['username']
        form_email=request.POST['email']
        form_password1=request.POST['password1']
        form_password2=request.POST['password2']
        form_department=request.POST['department']
        form_catagory=request.POST['catagory']
        
        is_staff = False
        is_superuser = False
        
        if form_password1 != form_password2:
            messages.info(request,message="passwords don't match")
            return redirect('/services/add_user')

        if User.objects.filter(first_name=form_first_name,last_name=form_last_name).exists():
            messages.info(request,message='only one account allowed per user')
            return redirect('/services/add_user')

        if User.objects.filter(username=form_user_name).exists():
            messages.info(request,message='username taken')
            return redirect('/services/add_user')



        if str(form_catagory) == "system_admin":
            is_superuser=True

        if str(form_catagory) != "end_user":
            is_staff=True
        

        user = User.objects.create(first_name = form_first_name,last_name=form_last_name,
                username=form_user_name,email=form_email,department=form_department,
                catagory=form_catagory,is_staff=is_staff,is_active=True,
                is_superuser=is_superuser)

        user.set_password(form_password1)

        user.save()
        messages.info(request,message='user successfully added')
        return redirect('/services/add_user')


        

        