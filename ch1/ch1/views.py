#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:20:23 2020

@author: dhk1349
"""

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='home.html'