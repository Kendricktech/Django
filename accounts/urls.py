from django.contrib import admin
from django.urls import path,include
from .views import index
import views

app_name='accounts'
urlpatterns = [
   path('register/',views.register,name='register'),

]
