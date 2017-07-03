# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
    user = models.ForeignKey(User)
    priority = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=100)


class Restriction(models.Model):
    MIN_DUR = "min"
    MAX_DUR = "max"
    CHOICES = ((MIN_DUR, "Minimum Duration"), (MAX_DUR, "Maximum Duration"))

    item = models.ForeignKey(Item)
    rtype = models.CharField(max_length=3, choices=CHOICES)
    value = models.CharField(max_length=20)
