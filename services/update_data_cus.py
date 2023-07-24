from django.shortcuts import render


def update_data_cus(request):
    if request.method == "GET":
        return render(request,'services/update_data.html')

    else:
        pass