from django.shortcuts import render

# Create your views here.
def online(req):
    return render(req,'online.html')
def offline(req):
    return render(req,'offline.html')
def company(req):
    return render(req,'company.html')