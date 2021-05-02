# templates/main/home.html
from django.shortcuts import render

# Create your views here.

# homePage views
def homePage(request):
    return render(request, 'main/home.html')

# aboutPage views
def aboutPage(request):
    return render(request, 'main/about.html')