#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:26:25 2020

@author: dhk1349
"""

from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV

app_name='bookmark'

urlpatterns = [

    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
    
]
