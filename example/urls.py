# example/urls.py
from django.urls import path

# from example.views import index
from example.views import index,getWazirxData
from django.urls import re_path


urlpatterns = [
    path('', index),
re_path(r'^api/getAnalyticalData$', getWazirxData),
]