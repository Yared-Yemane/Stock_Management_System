from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth, messages
from django.http import HttpResponse


from .models import Inventory, OfficerPenRequest, DirectorPenRequest
from .models import ProcessedRequest, UserNotifications
#from .request_item_cus import initiate_request
from .request_item_cus import request_item_cus


User = get_user_model()

def retry_cus(request,item_request_id):

    item_request = UserNotifications.objects.get(cus_id =str(item_request_id))
    previous_info = [item_request.additional_info[0],item_request.additional_info[1],
                    item_request.additional_info[2],item_request.additional_info[3],
                    item_request.additional_info[4]]

    items = Inventory.objects.all()


    if request.method == 'GET':
        print(item_request_id)
        return render(request,'services/retry_request.html', {'curr_item_name':previous_info[0],'item_amount':previous_info[1],
                                                               'duty':previous_info[2],'director':previous_info[3],
                                                                'description':previous_info[4],
                                                                 'items':items,'item_request_id':str(item_request_id)})

                                    

    else:

        """print(request.POST.get('item_name'))
        return HttpResponse(request.POST.get('item_name'))"""

        if request.POST.get('cancel'):
            return redirect('/')

        form_item_name=request.POST['item_name']
        form_item_amount=request.POST['item_amount']
        form_user_duty = request.POST['user_duty']
        form_receiver = request.POST['receiver']
        form_description = request.POST['description']

        new_info = [form_item_name, form_item_amount, form_user_duty, form_receiver, form_description]

        no_change = (previous_info[0] == new_info[0] and previous_info[1] == new_info[1] and
                     previous_info[2] == new_info[2] and previous_info[3] == new_info[3] and
                     previous_info[4] == new_info[4])

        #print(no_change, no_change_0)

        if no_change:
            messages.info(request, message='Please make some changes')
            return redirect('/request_item/retry/'+str(item_request_id))

        else:
            if int(form_item_amount) <= 0:
                messages.info(request,message="invalid item amount, must be > 0")
                return redirect('/request_item/retry/'+str(item_request_id))

            item=Inventory.objects.get(item_name=form_item_name)
            #print(form_item_name)
            #print(item)

            if int(form_item_amount) > int(item.item_amount):
                messages.info(request,message="requested amount is > storage amount")
                return redirect('/request_item/retry/'+str(item_request_id))

            else:
                if str(request.user.catagory) == "director":
                    item_request = OfficerPenRequest.objects.create(cus_id = str(item_request_id),
                                    item_name=form_item_name,
                                    item_amount=form_item_amount,first_name=request.user.first_name,
                                    last_name=request.user.last_name,username = request.user.username,
                                    user_department=request.user.department,user_duty=form_user_duty,
                                    officer_fullname=form_receiver, director_description = form_description)
                                    
                    item_request.save()


                else:
                    item_request = DirectorPenRequest.objects.create(cus_id = str(item_request_id),
                                    item_name=form_item_name,
                                    item_amount=form_item_amount,first_name=request.user.first_name,
                                    last_name=request.user.last_name,username=request.user.username,
                                    user_department=request.user.department,
                                    user_duty=form_user_duty,director_fullname=form_receiver, user_description = form_description)
            
                    item_request.save()
                    print('request created')

                messages.info(request,message="request delivered")
                UserNotifications.objects.filter(cus_id = item_request_id).delete()
                return redirect('/')