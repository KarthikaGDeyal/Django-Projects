from django.shortcuts import render,redirect
from ShopApp.models import Registration_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
def shop_page(request):
    return render(request,"Shop.html")

def register_page(request):
    return render(request,'Register.html')

def registration_data(request):
    if request.method=="POST":
        f = request.POST.get('shop_name')
        g = request.POST.get('place_name')
        h = request.POST.get('mobile_no')
        i = request.POST.get('owner_name')
        j = request.POST.get('shop_type')
        img = request.FILES['image']
        obj=Registration_Db(ShopName=f,Place=g,Mobile=h,OwnerName=i,ShopType=j,ProfileImage=img)
        obj.save()
        return redirect('register_page')

def display_registration(request):
    data = Registration_Db.objects.all()
    return render(request, "Display_Registration.html", {'data': data})



def edit_registration(request,emp_id):
    data=Registration_Db.objects.get(id=emp_id)
    return render(request,"Edit_Registration.html",{'data':data})

def update_registration(request,emp_id):
    if request.method=="POST":
        f = request.POST.get('shop_name')
        g = request.POST.get('place_name')
        h = request.POST.get('mobile_no')
        i = request.POST.get('owner_name')
        j = request.POST.get('shop_type')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Registration_Db.objects.get(id=emp_id).ProfileImage
        Registration_Db.objects.filter(id=emp_id).update(ShopName=f, Place=g, Mobile=h,OwnerName=i,ShopType=j, ProfileImage=img)
        return redirect('display_registration')
def delete_registration(request,emp_id):
    x=Registration_Db.objects.filter(id=emp_id)
    x.delete()
    return redirect('display_registration')

# Create your views here.
