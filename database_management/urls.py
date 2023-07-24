from django.contrib import admin
from django.urls import path,include

from . import views
from accounts.views import home
from services.views import retry

urlpatterns = [
    path('update_data', views.update_data, name='update_data'),
    path('update_data', views.update_data, name='update_data'),
    path('update_data', views.update_data, name='update_data'),

]
