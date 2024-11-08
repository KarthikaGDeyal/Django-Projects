from django.shortcuts import render,redirect
from TextApp1.models import DemoDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
def index_page(request):
    return render(request,'index.html')

def demo_page(req):
    return render(req,'Demo.html')

def save_demo(request):
    if request.method=="POST":
        a= request.POST.get('cat_name')
        b = request.POST.get('cat_desc')
        img = request.FILES['image']
        obj=DemoDb(CategoryName=a,Description=b,CategoryImage=img)
        obj.save()
        return redirect('demo_page')

def view_details(request):
    data = DemoDb.objects.all()
    return render(request, "View_Details.html", {'data':data})



def edit_details(request,cat_id):
    data=DemoDb.objects.get(id=cat_id)
    return render(request,"Edit_Details.html",{'data':data})

def update_details(request,cat_id):
    if request.method=="POST":
        a = request.POST.get('cat_name')
        b = request.POST.get('cat_desc')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=DemoDb.objects.get(id=cat_id).CategoryImage
        DemoDb.objects.filter(id=cat_id).update(CategoryName=a,Description=b,CategoryImage=file)
        return redirect('view_details')
def delete_details(request,cat_id):
    x=DemoDb.objects.filter(id=cat_id)
    x.delete()
    return redirect('view_details')



# Create your views here.



