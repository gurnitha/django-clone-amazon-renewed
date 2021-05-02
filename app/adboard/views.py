# app/adboard/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# homeAdmin to render admin home page
def adminHome(request):
	return render(request, 'adboard/admin_home.html')

# loginAdmin to render login page
def adminLogin(request):
	return render(request, 'adboard/admin_login.html')

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
		return HttpResponseRedirect(reverse('admin_home'))

	# If user not exist in db
	else:
		messages.error(request, 'Login error! Invalid login detail!')
		return HttpResponseRedirect(reverse('admin_login'))

# # Logout
# def adminLogoutProcess(request):
# 	logout(request)
# 	messages.success(request, 'Logout successfully!')
# 	return HttpResponseRedirect(reverse('admin_login')

def adminLogoutProcess(request):
	logout(request)
	messages.success(request, 'Logged out successfully!')
	return HttpResponseRedirect(reverse('admin_login'))