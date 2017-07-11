# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from logging import getLogger
from .models import Item, Restriction

logger = getLogger(__name__)

def todo_list(request):
    user = request.user
    items = Item.objects.filter(user=user).order_by('priority')

    return render(request, 'todo_list.html', {"items": items, "user": user})


def detail(request, pk):
    user = request.user
    todo_item = Item.objects.filter(user=user).filter(pk=pk).first
    if todo_item:
        return render(request, 'detail.html', {"todo_item": todo_item, "user": user})
    else:
        return HttpResponse("Not Found")


def login(request):
    return render(request, 'login.html', {"request": request, "user": request.user})


def user_login(request):
    return render(request, 'login_form.html', {'request': request})


def user_password(strategy, user, *args, **kwargs):
    if strategy.backend.name != 'username':
        return

    logger.info("Setting password to default")
    user.set_password("")
    user.save()
