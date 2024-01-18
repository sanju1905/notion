from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('hello-viewset',HelloViewSet,basename='hello-viewset')
urlpatterns = [
    path('create_user/', Create_User, name='create_user'),
    path('',include(router.urls))
   
]