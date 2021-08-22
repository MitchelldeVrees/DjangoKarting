from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('signup/', sign_up_view),
    
    path('login_user', views.login_user, name="login"),


    
    
]

