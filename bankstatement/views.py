# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import files
from . serializers import FilesSerializer

# Create your views here.

class fileslist(APIView):
	def get(self, request):
		files1 = files.objects.all()
		serializers=FilesSerializer(files1, many=True)
		return Response(serializers.data)

	def post(self):
		pass	
	

