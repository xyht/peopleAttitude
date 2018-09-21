from django.urls import path
from .views import index

urlpatterns = [
    path('upload/setupload/', index.setupload),
    path('upload/getupload/', index.getupload),
    path('upload/getuploadvideo/',index.getuploadvideo)
]
# -*- coding: utf-8 -*-
