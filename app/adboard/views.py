# app/adboard/views.py
from django.shortcuts import render

# Create your views here.

def homePageAdboard(request):
	return render(request, 'adboard/home-adboard.html')
