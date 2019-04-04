from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# =======================tests1===========================
# def home_page():
#     pass

# ========================tests2===========================
# def home_page(request):
#     return HttpResponse('<html><title>Django</title></html>')

def home_page(request):
    return render(request,'home.html')