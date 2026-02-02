from django.shortcuts import render

def home(request):
    return render(request, 'nzc/base/home.html')
