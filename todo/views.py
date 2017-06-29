# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def todo_list(request):
    return render(request, 'todo_list.html')
#    return HttpResponse("This is your to-do list!")