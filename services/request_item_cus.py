from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime

from .models import Inventory, OfficerPenRequest, DirectorPenRequest
from .models import ProcessedRequest, UserNotifications

from .generate_id import generate_id
# Create your views here.

"""def initiate_request(request,inputs):
    if int(inputs[1]) <= 0:
            messages.info(request,message="invalid item amount, must be > 0")
            return redirect('/services/request_item')

    item=Inventory.objects.get(item_name=inputs[0])
        #print(form_item_name)
        #print(item)
        # 
    if int(inputs[1]) > int(item.item_amount):
        messages.info(request,message="requested amount is > storage amount")
        return redirect('/services/request_item')

    else:
        if str(request.user.catagory) == "director":
            item_request = OfficerPenRequest.objects.create(cus_id = str(request.user.username+str(datetime.now())),
                            item_name=inputs[0],
                            item_amount=inputs[1],first_name=request.user.first_name,
                            last_name=request.user.last_name,username = request.user.username,
                            user_department=request.user.department,user_duty=inputs[2],
                            officer_fullname=inputs[3])
                                
            item_request.save()


        else:
            item_request = DirectorPenRequest.objects.create(cus_id = str(request.user.username+str(datetime.now())),
                            item_name=inputs[0],
                            item_amount=inputs[1],first_name=request.user.first_name,
                            last_name=request.user.last_name,username=request.user.username,
                            user_department=request.user.department,
                            user_duty=inputs[2],director_fullname=inputs[3])
          
            item_request.save()

        messages.info(request,message="request delivered")
        return redirect('/')"""


def request_item_cus(request):
    if request.method == "GET":

        #DirectorPenRequest.objects.all().delete()
        #OfficerPenRequest.objects.all().delete()
        #UserNotifications.objects.all().delete()
        #ProcessedRequest.objects.all().delete()

        items = Inventory.objects.all()
        return render(request,'services/request_item.html',{'items':items})

    else:
        form_item_name=request.POST['item_name']
        form_item_amount=request.POST['item_amount']
        form_user_duty = request.POST["user_duty"]
        form_receiver = request.POST["receiver"]
        form_description = request.POST['description']

        #cus_inputs = [form_item_name,form_item_amount,form_user_duty,form_receiver]

        #return initiate_request(request,cus_inputs)

        if int(form_item_amount) <= 0:
            messages.info(request,message="invalid item amount, must be > 0")
            return redirect('/services/request_item')

        item=Inventory.objects.get(item_name=form_item_name)
        #print(form_item_name)
        #print(item)

        if int(form_item_amount) > int(item.item_amount):
            messages.info(request,message="requested amount is > storage amount")
            return redirect('/services/request_item')

        else:
            if str(request.user.catagory) == "director":
                item_request = OfficerPenRequest.objects.create(cus_id = generate_id(),
                                item_name=form_item_name,
                                item_amount=form_item_amount,first_name=request.user.first_name,
                                last_name=request.user.last_name,username = request.user.username,
                                user_department=request.user.department,user_duty=form_user_duty,
                                officer_fullname=form_receiver, director_description = form_description)
                                
                item_request.save()


            else:
                item_request = DirectorPenRequest.objects.create(cus_id = generate_id(),
                                item_name=form_item_name,
                                item_amount=form_item_amount,first_name=request.user.first_name,
                                last_name=request.user.last_name,username=request.user.username,
                                user_department=request.user.department,
                                user_duty=form_user_duty,director_fullname=form_receiver, user_description = form_description)
          
                item_request.save()
                print('request created')

            messages.info(request,message="request delivered")
            return redirect('/')

        #return HttpResponse("working")
    




