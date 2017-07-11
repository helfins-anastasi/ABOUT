# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from social_django.models import USER_MODEL



class Item(models.Model):
    user = models.ForeignKey(USER_MODEL)
    priority = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s (%s #%d)' % (self.title, self.user, self.priority)

    def url(self):
        return str(self.pk)


class Restriction(models.Model):
    MIN_DUR = "min"
    MAX_DUR = "max"
    CHOICES = ((MIN_DUR, "Minimum Duration (minutes)"), (MAX_DUR, "Maximum Duration (minutes)"))

    item = models.ForeignKey(Item)
    rtype = models.CharField(max_length=3, choices=CHOICES)
    cvalue = models.CharField(max_length=20, blank=True)
    ivalue = models.IntegerField(blank=True)

    def __str__(self):
        if self.rtype == Restriction.MIN_DUR or self.rtype == Restriction.MAX_DUR:
            return '%s of %dmin for %s' % (self.rtype, self.ivalue, self.item)
        else:
            return '%s (%s)' % (self.rtype, self.item)
