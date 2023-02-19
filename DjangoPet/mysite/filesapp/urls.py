
# -*- coding: utf-8 -*-
from django.urls import path, re_path


from . import views

urlpatterns = [
    # path('', views.MainView.as_view(), name='filesapp_view'),
    path('', views.index, name='filesapp_view'),
    path('upload/', views.file_upload_view, name='filesapp_upload'),
    path('upload2/', views.doc_upload_view, name='filesapp_upload2'),
    # path('filesapp/upload/', views.file_upload_view),
]