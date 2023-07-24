from django.urls import path
from . import views


urlpatterns = [
    path('login', views.user_login,name='user_login'),
    path('logout',views.user_logout,name='user_logout'),
    path('login/change_pw',views.change_pw,name='change_pw'),
    #path('recover_pw',views.recover_pw,name='recover_pw'),
]
