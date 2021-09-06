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

urlpatterns = [
    path('', homepage_view, name='home'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('login_user', login_user, name="login"),
    path('logout_user', logout_user, name="logout"),
    path('register_user', register_user, name="register"),
    path('drivers/', driver_detail_view),
    path('competition/', standing_view),
    path('adddriver/', create_driver),
    path('updatedriver/<str:id>/', update_driver, name="update_driver"),
    path('deletedriver/<str:id>/', delete_driver, name="delete_driver"),
    path('reset_password/', auth_views.PasswordResetView.as_view()),



    path('admin/', admin.site.urls),
    
    
]

