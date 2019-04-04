from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# =======================tests1===========================
# def home_page():
#     pass

# ========================tests2===========================
# def home_page(request):
#     return HttpResponse('<html><title>Django</title></html>')

# ======================test3--test4=======================
# def home_page(request):
#     if request.method=='POST':
#         return HttpResponse(request.POST['item_text'])
#     return render(request,'home.html')

# ======================test5=======================
def home_page(request):
    return render(request,
                  'home.html',{
                      'new_item_text':request.POST.get('item_text',''),
                  })