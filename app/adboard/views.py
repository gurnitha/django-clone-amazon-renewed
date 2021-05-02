# app/adboard/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# homeAdmin to render admin home page
def homeAdmin(request):
	return render(request, 'adboard/home-admin.html')

# loginAdmin to render login page
def loginAdmin(request):
	return render(request, 'adboard/login-admin.html')

# Process and authenticate user login
def adminLoginProcess(request):
	
	# Get input from the login form page
	username=request.POST.get('username')
	password=request.POST.get('password')

	# Authenticate user credentials
	user=authenticate(
		request=request,username=username,password=password)

	# If user exist in db
	if user is not None:
		login(request=request, user=user)
		return HttpResponseRedirect(reverse('home_admin'))

	# If user not exist in db
	else:
		messages.error(request, 'Login error! Invalid login detail!')
		return HttpResponseRedirect(reverse('login_admin'))

