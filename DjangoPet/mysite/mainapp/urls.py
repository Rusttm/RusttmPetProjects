# -*- coding: utf-8 -*-
from django.urls import path, re_path


from . import views

urlpatterns = [
    path('', views.index, name='mainapp_view'),
    path('main', views.MainView.as_view(), name='mainapp_view1'),

]