# app/adboard/views.py
from django.shortcuts import render

# Create your views here.

def homeAdmin(request):
	return render(request, 'adboard/home-admin.html')

def loginAdmin(request):
	return render(request, 'adboard/login-admin.html')
