# app/adboard/views.py
from django.shortcuts import render

# Create your views here.

# homeAdmin to render admin home page
def homeAdmin(request):
	return render(request, 'adboard/home-admin.html')

# loginAdmin to render login page
def loginAdmin(request):
	return render(request, 'adboard/login-admin.html')

# adminLoginProcess to process the login without rendering any page
def adminLoginProcess(request):
	return render(request, 'backend/login_admin_process.html')