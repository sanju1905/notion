from django.urls import path
from .views import Create_User

urlpatterns = [
    path('create_user/', Create_User, name='create_user'),
   
]