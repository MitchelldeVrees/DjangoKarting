"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views

from pages.views import homepage_view, standing_view
from drivers.views import driver_detail_view, create_driver, update_driver, delete_driver
from users.views import login_user,logout_user, register_user, forgot_password
from competitions.views import competition_detail_view,create_competition,see_competition
from races.views import create_race

urlpatterns = [
    path('', homepage_view, name='home'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('login_user', login_user, name="login"),
    path('logout_user', logout_user, name="logout"),
    path('register_user', register_user, name="register"),

    path('competitions/', competition_detail_view),
    path('addcompetitions/', create_competition),
    # path('updatecompetition/<str:id>/', update_competition),
    # path('deletecompetition/<str:id>/', delete_competition),
    path('seecompetition/<str:id>/', see_competition),

    path('addrace/',create_race),


    path('drivers/', driver_detail_view),
    path('adddriver/', create_driver),
    path('updatedriver/<str:id>/', update_driver, name="update_driver"),
    path('deletedriver/<str:id>/', delete_driver, name="delete_driver"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_send.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),
    



    path('admin/', admin.site.urls),
    
    
]

