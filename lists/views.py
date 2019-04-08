from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List
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
# def home_page(request):
#     return render(request,
#                   'home.html',{
#                       'new_item_text':request.POST.get('item_text',''),
#                   })

# ======================test7=======================
# def home_page(request):
#     item = Item()
#     item.text = request.POST.get('item_text','')
#     item.save()
#     return render(request,
#                   'home.html',{
#                       'new_item_text':item.text,
#                   })


# ======================test8=======================
# def home_page(request):
#     if request.method=='POST':
#         new_item_text = request.POST['item_text']
#         Item.objects.create(text=new_item_text)
#     else:
#         new_item_text=''
#     return render(request,'home.html',{'new_item_text':new_item_text,})

# ======================test9=======================
# def home_page(request):
#     if request.method=='POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/')
#     return render(request,'home.html')


# ======================test10=======================
# def home_page(request):
#     if request.method=='POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/')
#     items = Item.objects.all()
#     return render(request,'home.html',{"items":items})

# ======================test11=======================
# def home_page(request):
#     if request.method=='POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/lists/the-only-list-in-the-world/')
#     # items = Item.objects.all()
#     # return render(request,'home.html',{"items":items})
#     return render(request,'home.html')

# ======================test12=======================
def view_list(request,list_id):
    print('&&&&&&&&&&view_list&&&&&&&&&&&&')
    list_ = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_)
    # return render(request, 'list.html', {"items": list_})
    return render(request, 'list.html', {"list": list_})
# ======================test14=======================
def new_list(request):
    print('&&&&&&&&&&new_list&&&&&&&&&&&&')
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')

def home_page(request):
    print('&&&&&&&&&&home_page&&&&&&&&&&&&')
    return render(request,'home.html')

# ======================test17=======================
def add_item(request,list_id):
    print('&&&&&&&&&&add_item&&&&&&&&&&&&')
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')