#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:xuyukun
@file: views.py
@time: 2018/11/24

"""

from django.shortcuts import render_to_response

def home(request):
    context= {}
    return render_to_response('home.html', context)