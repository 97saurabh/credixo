from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register/',views.registration,name = "register"),
    path('login/',obtain_auth_token,name="login"),
]
