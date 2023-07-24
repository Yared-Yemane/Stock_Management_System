from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


from .models import DirectorPenRequest, OfficerPenRequest, ProcessedRequest


def get_notifications_cus(request):
    #DirectorPenRequest.objects.all().delete()
    #OfficerPenRequest.objects.all().delete()
    #ProcessedRequest.objects.all().delete()

    if request.method == 'GET':
        requests = []

        if request.user.catagory == 'director':
            requests = DirectorPenRequest.objects.all()

        elif request.user.catagory == 'officer':
            requests = OfficerPenRequest.objects.all()

        else:
            requests = ProcessedRequest.objects.filter(username = request.user.username)
        
        if len(requests) == 0:
            messages.info(request,message='You have no notificcations')
            #print(len(requests))
            return redirect('/')

        return render(request,'services/notifications.html',{'requests':requests})


    else:
        pass
