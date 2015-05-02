# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import *


class Menu(models.Model):
    name = models.CharField(max_length=200)
    pos = models.IntegerField()

    def __unicode__(self):
    	return "%s (%d)" % (self.name, self.pos)


class SubMenu(models.Model):
    name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu)
    pos = models.IntegerField()


    link = models.CharField(max_length=500)
    extern = models.BooleanField(default=False)
    superuser_only = models.BooleanField(default=False)

    permissions = models.ManyToManyField(Permission, blank=True, null=True)

    def __unicode__(self):
    	return self.name
