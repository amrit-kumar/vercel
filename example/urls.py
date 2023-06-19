# example/urls.py
from django.urls import path

# from example.views import index
from example import views
from example.views import getWazirxData
from django.urls import re_path
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import  login


urlpatterns = [
    # path('', index),
    path('', include(router.urls)),
re_path(r'^api/getAnalyticalData$', getWazirxData),


    path('api/login', login),
    re_path(r'^api/register', csrf_exempt(views.CreateUserView.as_view())),

    re_path(r'^api/profile/', views.profile),

    re_path(r'^api/getWazirxData$', views.getWazirxData),
    re_path(r'^api/getHistoricalData/', views.getHistoricalData),
]