#!usr/bin/python
# -*- coding:utf-8 -*-
# __author = 'Bruce.张'


from django.urls import path
from . import views

urlpatterns = [
    path('', views.queryall),
    path('page/<int:num>/', views.queryall),
    path('post/<int:post_id>/', views.detail),
    path('category/<int:cate_id>/', views.cateshow),
    path('archive/<int:year>/<int:month>/', views.bycreated),
]