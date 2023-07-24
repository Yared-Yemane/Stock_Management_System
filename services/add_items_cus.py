from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Inventory


def add_items_cus(request):
    if request.method == "GET":
        return render(request,'services/add_items.html')

    else:
        #form_item_catagory = request.POST['item_catagory']
        form_item_name = request.POST['item_name']
        form_item_amount = request.POST['item_amount']

        if int(form_item_amount) <= 0:
            messages.add_message(request,message="invalid amount")
            return redirect('/services/add_items')

        item = Inventory.objects.filter(item_name=form_item_name).exists()
        print(item)


        if item is not False:
           # return HttpResponse("added")
            item=Inventory.objects.get(item_name=form_item_name)
            item.item_amount= int(form_item_amount)+int(item.item_amount)
            item.save()
            messages.info(request,message="Item already exists, and successfully updated")
            return redirect('/services/add_items')

        else:
            item=Inventory.objects.create(item_name=form_item_name,item_amount=form_item_amount)
            item.save()
            messages.info(request,message="Item successfully added")
            return redirect('/services/add_items')







