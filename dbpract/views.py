from django.shortcuts import render
import random
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def password(request):
    char = list('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*_+\/><~')
    password = ''
    for i in range(15):
        password += random.choice(char)
    pas = {'password':password}
    return JsonResponse(pas)