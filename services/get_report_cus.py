from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime

from .models import Inventory, OfficerPenRequest, DirectorPenRequest
from .models import ProcessedRequest, UserNotifications

from .generate_id import generate_id

def get_report_cus(request):
    if request.method == 'GET':
        return render(request,'services/get_report.html')

    else:
        pass