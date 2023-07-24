from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib import messages

from services.models import Inventory

# Create your views here.

def update_data(request):

    items = Inventory.objects.all()


    if request.method == 'GET':


        return render(request, 'database_management/update_data.html',{'items':items})

    else:
        if request.POST.get('update'):
            form_item_names = request.POST.getlist('form_item_name')
            form_item_amounts = request.POST.getlist('form_item_amount')

            iteration_index = 0

            for form_item_name in form_item_names:
                if not form_item_name:
                    break

                if Inventory.objects.filter(item_name=form_item_name).exists():
                    db_item = Inventory.objects.get(item_name = form_item_name)
                    db_item.item_amount = int(db_item.item_amount) + int(form_item_amounts[iteration_index])
                    db_item.save()

                else:
                    new_item = Inventory.objects.create(item_name = form_item_name, 
                                                        item_amount = form_item_amounts[iteration_index])

                    new_item.save()
                
                iteration_index = iteration_index + 1

            messages.info(request,message='database successfully updated')

            return redirect('/')

        else:
            return redirect('/database/update_data')

            


        """#form_item_name = cus_values.get("form_item_name")
        #my_form = YourForm()

        #print(form_item_names)
        print(form_item_amounts[3])


        return HttpResponse('working . . .')"""