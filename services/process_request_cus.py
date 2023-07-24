from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime

from .models import DirectorPenRequest, OfficerPenRequest
from .models import UserNotifications, ProcessedRequest, Inventory

def process_request_cus(request, item_request_id):

    request_obj = None

    if request.user.catagory == 'director':
        request_obj = DirectorPenRequest.objects.get(cus_id=str(item_request_id))

    elif request.user.catagory == 'officer':
        request_obj = OfficerPenRequest.objects.get(cus_id=str(item_request_id))

    else:
        request_obj = ProcessedRequest.objects.get(cus_id=str(item_request_id))

    print(request_obj)

    if request_obj is None:
        return HttpResponse('object none')

    if request.method == "GET":
        #print(request_obj)
        #print(request.method.value,"value--")
        return render(request,'services/process_request.html',{'request_obj':request_obj})

    else:
 
        if not request.POST.get('back'):

            if request.POST.get('proceed'):

                cus_message = ""
                """if request.user.catagory == 'director':
                    UsedModel = OfficerPenRequest
                else:
                    UsedModel = DirectorPenRequest"""

                responder = None
                if request.user.catagory == 'director':

                    off_pen_req = OfficerPenRequest.objects.create(cus_id = str(item_request_id),
                                    item_name=request_obj.item_name,item_amount=request_obj.item_amount,
                                    first_name=request_obj.first_name,last_name=request_obj.last_name,
                                    username=request_obj.username,user_department=request_obj.user_department,
                                    user_duty=request_obj.user_duty)

                    off_pen_req.approval = 'accepted'

                    DirectorPenRequest.objects.filter(cus_id=str(item_request_id)).delete()       

                    messages.info(request,message='request has been accepted, and proceeded to officer')

                    cus_message = ('Your item request for ' + str(request_obj.item_amount) +"(s) "+ str(request_obj.item_name)
                                    + ' has been approved by director and proceeded to officer.')

                else:
                    inventory = Inventory.objects.get(item_name=request_obj.item_name)
                    #print(inventory.item_name)
                    inventory.item_amount = inventory.item_amount - request_obj.item_amount
                    #print(request_obj)
                    inventory.save()

                    cus_message = ('Your item request for ' + str(request_obj.item_amount) +"(s) "+ str(request_obj.item_name)
                                    + ' has been successfully completed.')

                    messages.info(request,message='Request successfully processed')
                    
                    OfficerPenRequest.objects.filter(cus_id=item_request_id).delete()       

            elif request.POST.get('notify'):
                request_obj.notified = True
                request_obj.save()
                cus_message = ('You are being requested to report in person for your previous request of' + 
                                str(request_obj.item_amount) + str(request_obj.item_name)+"(s)")

                messages.info(request,message='User successfully notified')
                                       
                """print(request_obj.item_name)
                print('notification successful')
                print(request_obj.notified)"""

                #return redirect('/services/process_request/'+item_request_id)

            else:

                messages.info(request,message='request has been rejected and sent back to, '
                             +request_obj.first_name+" "+request_obj.last_name)

                cus_message = ('Unfortunately, your item request for ' + str(request_obj.item_amount) 
                                + str(request_obj.item_name)+"(s) " + 'has been rejected by director.')
                
                DirectorPenRequest.objects.filter(cus_id=str(item_request_id)).delete()  

#----------------------------------userNotifications------------------------------------------------

            if (UserNotifications.objects.filter(cus_id=item_request_id).exists()):

                user_notification = UserNotifications.objects.get(cus_id=item_request_id)
                user_notification.cus_message = cus_message
                user_notification.save()

            else:
                cus_additional_info = [request_obj.item_name,request_obj.item_amount,
                                    request_obj.user_duty,request_obj.director_fullname,request_obj.user_description]

                user_notification = UserNotifications.objects.create(username = request_obj.username,
                                                                message = cus_message, cus_id = str(item_request_id),
                                                                 additional_info=cus_additional_info)
                
                user_notification.save()

#----------------------------------return values------------------------------------------------

        if request.POST.get('notify'):
            return redirect('/services/process_request/'+item_request_id)

        else:
            return redirect('/services/notifications')                



     

            
            #return HttpResponse('proceed')   
            #return redirect('/services/notifications')                

            """ else:
            return redirect('/services/notifications')"""