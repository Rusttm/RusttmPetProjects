# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='matplotapp_view'),
    path('index', views.index, name='matplotapp_index'),
    path('function', views.func_view, name='matplotapp_func'),

]