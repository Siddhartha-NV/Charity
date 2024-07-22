from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth 
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact-us.html')

def donate(request):
    return render(request, 'donate.html')

def thanks(request):
    return render(request, 'thanks.html')

