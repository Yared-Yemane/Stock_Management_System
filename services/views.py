from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .add_user_cus import add_user_cus
from .request_item_cus import request_item_cus
from .update_data_cus import update_data_cus
from .add_items_cus import add_items_cus
from .process_request_cus import process_request_cus
from .get_notifications_cus import get_notifications_cus
from .del_notf_cus import del_notf_cus
from .retry_cus import retry_cus
from .get_report_cus import get_report_cus

from .models import DirectorPenRequest, OfficerPenRequest, ProcessedRequest

# Create your views here.

def add_user(request):
    return add_user_cus(request)

def request_item(request):
    return request_item_cus(request)

def update_data(request):
    return update_data_cus(request)

def add_items(request):
    return add_items_cus(request)

def process_request(request, item_request_id):
    return process_request_cus(request, item_request_id)

"""def process_request(request,item_request_id):
    return HttpResponse("processing")"""

def get_notifications(request):
    return get_notifications_cus(request)

def del_notf(request, notification_id):
    return del_notf_cus(request, notification_id)

def retry(request, item_request_id):
    return retry_cus(request, item_request_id)

def get_report(request):
    return get_report_cus(request)