# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class files(models.Model):
	firstname=models.CharField(max_length=10)
	lastname=models.CharField(max_length=10)
	files_id = models.IntegerField()

	def __str__(self):
	 	return self.firstname 
