from django.shortcuts import render

def home(request):
    return render(request, 'client/base/home.html')
