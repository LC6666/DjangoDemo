from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# =======================test1===========================
# def home_page():
#     pass

def home_page(request):
    return HttpResponse('<html><title>Django</title></html>')
