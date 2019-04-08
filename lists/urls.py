# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'new$',views.new_list,name='new_list'),
    url(r'^(\d+)/$',views.view_list,name='new_list'),
    url(r'^(\d)/add_items$',views.add_item,name='add_item'),
]