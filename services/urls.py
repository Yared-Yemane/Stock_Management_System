from django.urls import path

from . import views


urlpatterns = [

    path('add_user', views.add_user,name='add_user'),
    path('request_item', views.request_item, name='request_item'),
    path('update_data', views.update_data, name='update_data'),
    path('add_items', views.add_items, name='add_items'),
    path('notifications', views.get_notifications,name="notifications"),
    path('process_request/<str:item_request_id>/',
          views.process_request, name='process_request'),
    path('notifications/del_notf/<str:notification_id>/',views.del_notf,name='del_notf'),
    path('request_item/retry/<str:item_request_id>/', views.retry, name='retry_request'),
    path('get_report',views.get_report, name='get_report'),

    #path('add_user', views.add_user,name='add_user'),

    #path('', home,name='home'),
    #path('auth',include('accounts.urls')),
    #path('services',include('services.urls')),
]
