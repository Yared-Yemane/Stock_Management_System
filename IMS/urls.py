from django.contrib import admin
from django.urls import path,include

from accounts.views import home, about, contact
from services.views import retry

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('auth/',include('accounts.urls')),
    path('services/',include('services.urls')),
    path('request_item/retry/<str:item_request_id>/', retry, name='retry_request'),
    path('about/',about, name="about"),
    path('contact/',contact, name="contact"),
    
]
