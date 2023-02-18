
# -*- coding: utf-8 -*-
from django.urls import path, re_path

import webapp

from . import views

urlpatterns = [
    path('', views.index, name='webapp_view'),
    path('example', views.example_page, name='webapp/example'),
    path('file', views.upload_file, name='uploader'),
    path('list', webapp.views.list, name='list'),
    re_path(r'^list/$', webapp.views.list),

]