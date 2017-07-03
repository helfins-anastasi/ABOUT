# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Item, Restriction


# Create your views here.
def todo_list(request, username):
    user = User.objects.get(name=username)
    items = Item.objects.filter(user=user).order_by('priority')

    return render(request, 'todo_list.html', {"items": items, "user": user})

def detail(request, username, pk):
    user = User.objects.get(name=username)
    todo_item = Item.objects.filter(user=user).filter(pk=pk).first
    if todo_item:
        return render(request, 'detail.html', {"todo_item": todo_item, "user": user})
    else:
        return HttpResponse("Not Found")
