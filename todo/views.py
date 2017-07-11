# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render, redirect
from logging import getLogger
from .models import Item, Restriction

logger = getLogger(__name__)


# Renders suggestion page
def suggest(request):
    user = request.user
    suggestion = Item.objects.filter(user=user).order_by('priority')[0]
    duration = "30 minutes"
    suggestion.url = get_url(suggestion)

    return render(request, 'suggest.html', {"suggestion": suggestion, "duration": duration, "user": user})


# Renders full list
def todo_list(request):
    user = request.user

    # This code is forcing evaluation of an otherwise lazy object – because we can't iterate on AnonymousUsers
    if hasattr(user, '_wrapped') and hasattr(user, '_setup'):
        if user._wrapped.__class__ == object:
            user._setup()
        user = user._wrapped
    if isinstance(user, AnonymousUser):
        return redirect(login)

    items = Item.objects.filter(user=user).order_by('priority')
    return render(request, 'todo_list.html', {"items": items, "user": user})


# Renders detailed view for a specific item (with identifier pk)
def detail(request, pk):
    user = request.user
    todo_item = Item.objects.filter(user=user).filter(pk=pk).first
    if todo_item:
        return render(request, 'detail.html', {"todo_item": todo_item, "user": user})
    else:
        return HttpResponse("Not Found")


# Renders login page
def login(request):
    return render(request, 'login.html', {"request": request, "user": request.user})


# Secret username login (for testing purposes)
def user_login(request):
    return render(request, 'login_form.html', {'request': request})


# ------------------- HELPER METHODS ------------------


def user_password(strategy, user, *args, **kwargs):
    if strategy.backend.name != 'username':
        return

    logger.info("Setting password to default")
    user.set_password("")
    user.save()
