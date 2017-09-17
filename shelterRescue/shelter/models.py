# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class Disaster(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    

class Shelter(models.Model):

    id = models.AutoField(primary_key=True)
    disaster = models.ForeignKey(Disaster, null=True, blank=True)
    name = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    capacity = models.IntegerField(null=True, blank=True)


class Person(models.Model):
	
    id = models.AutoField(primary_key=True)
    shelter = models.ForeignKey(Shelter, null=True, blank=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    emergencyName = models.CharField(max_length=32)
    emergencyPhone = models.CharField(max_length=32)
    emergencyEmail = models.CharField(max_length=32)
