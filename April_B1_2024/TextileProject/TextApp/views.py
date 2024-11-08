from django.shortcuts import render,redirect
from TextApp.models import DemoDb,ProDb
from Webapp.models import ContactDb,RegisterDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
def index_page(request):
    today=datetime.datetime.now()
    x= today.date()
    return render(request,'index.html',{'today': today,'x':x})

def demo_page(req):
    today = datetime.datetime.now()
    x = today.date()
    return render(req,'Demo.html',{'today': today,'x':x})

def save_demo(request):
    if request.method=="POST":
        a= request.POST.get('cat_name')
        b = request.POST.get('cat_des')
        img = request.FILES['image']
        obj=DemoDb(CategoryName=a,Description=b,CategoryImage=img)
        obj.save()
        messages.success(request,"Category saved successfully")
        return redirect('demo_page')

def view_details(request):
    today = datetime.datetime.now()
    x = today.date()
    data = DemoDb.objects.all()
    return render(request, "View Details.html", {'data': data,'today': today,'x':x})



def edit_details(request,cat_id):
    today = datetime.datetime.now()
    x = today.date()
    data=DemoDb.objects.get(id=cat_id)
    return render(request,"Edit_Details.html",{'data':data,'today': today,'x':x})

def update_details(request,cat_id):
    if request.method=="POST":
        a = request.POST.get('cat_name')
        b = request.POST.get('cat_des')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=DemoDb.objects.get(id=cat_id).CategoryImage

        DemoDb.objects.filter(id=cat_id).update(CategoryName=a,Description=b,CategoryImage=file)
        messages.success(request, "category updated successfully")

        return redirect('view_details')
def delete_details(request,cat_id):
    x=DemoDb.objects.filter(id=cat_id)
    x.delete()
    messages.success(request, "category deleted successfully")
    return redirect('view_details')


def product_page(req):
    today = datetime.datetime.now()
    x = today.date()
    demo=DemoDb.objects.all()
    return render(req,'Add_Product.html',{'demo':demo,'today': today,'x':x})

def save_product(request):
    if request.method=="POST":
        a= request.POST.get('cat_name')
        b = request.POST.get('pro_name')
        c = request.POST.get('pro_des')
        d = request.POST.get('price')
        e = request.POST.get('brand')
        img = request.FILES['image']
        img1 = request.FILES['image1']
        img2 = request.FILES['image2']

        obj=ProDb(CategoryName=a,ProductName=b,Description=c,Price=d,BrandName=e,ProductImage=img,ProductImage1=img1,ProductImage2=img2)
        obj.save()
        messages.success(request, "Product saved successfully")
        return redirect('product_page')

def product_details(request):
    today = datetime.datetime.now()
    x = today.date()
    data = ProDb.objects.all()
    return render(request, "Product_Details.html", {'data': data,'today': today,'x':x})



def edit_product(request,pro_id):
    today = datetime.datetime.now()
    x = today.date()
    cat=DemoDb.objects.all()
    data=ProDb.objects.get(id=pro_id)
    return render(request,"Edit_Product.html",{'cat':cat,'data': data,'today': today,'x':x})

def update_product(request,pro_id):
    if request.method=="POST":
        a = request.POST.get('cat_name')
        b = request.POST.get('pro_name')
        c = request.POST.get('pro_des')
        d = request.POST.get('price')
        e = request.POST.get('brand')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)

        except MultiValueDictKeyError:
            file=ProDb.objects.get(id=pro_id).ProductImage
        try:
            img = request.FILES['image1']
            fs = FileSystemStorage()
            file1 = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file1 = ProDb.objects.get(id=pro_id).ProductImage1
        try:
            img = request.FILES['image2']
            fs = FileSystemStorage()
            file2 = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file2 = ProDb.objects.get(id=pro_id).ProductImage2
        ProDb.objects.filter(id=pro_id).update(CategoryName=a,ProductName=b,Description=c,Price=d,BrandName=e,ProductImage=file,ProductImage1=file1,ProductImage2=file2)
        messages.success(request, "product updated successfully")
        return redirect('product_details')
def delete_product(request,pro_id):
    x=ProDb.objects.filter(id=pro_id)
    x.delete()
    messages.success(request, "product deleted successfully")
    return redirect('product_details')

def admin_page(request):
    return render(request, 'admin.html')

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request,"Welcome...!!")
                return redirect(index_page)
            else:
                messages.warning(request,"Invalid username or password")
                return redirect(admin_page)
        else:
            messages.warning(request,"User not found")
            return redirect(admin_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_page)

def contact_page(request):
    today = datetime.datetime.now()
    x = today.date()
    data=ContactDb.objects.all()
    return render(request,"ContactDetails.html",{'data': data,'today': today,'x':x})

def delete_contact(request,co_id):
    x=ContactDb.objects.filter(id=co_id)
    x.delete()
    return redirect(contact_page)

def register_page(request):
    today = datetime.datetime.now()
    x = today.date()
    data=RegisterDb.objects.all()
    return render(request,"RegisterDetails.html",{'data': data,'today': today,'x':x})

def delete_registration(request,re_id):
    x=RegisterDb.objects.filter(id=re_id)
    x.delete()
    return redirect(register_page)







# Create your views here.
