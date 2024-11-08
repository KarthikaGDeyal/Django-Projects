from django.shortcuts import render,redirect
from EmpApp.models import EmployeeDb,Registration_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

def index_page(request):
    return render(request,'index.html')

def employee_page(request):
    return render(request,'Add_Employee.html')

def display_employee(request):
    data = EmployeeDb.objects.all()
    return render(request, "Display_Employee.html", {'data': data})

def save_employee(request):
    if request.method=="POST":
        a= request.POST.get('emp_name')
        b = request.POST.get('emp_email')
        c = request.POST.get('emp_mobile')
        d = request.POST.get('emp_salary')
        e = request.POST.get('emp_place')
        obj=EmployeeDb(Name=a,Email=b,Mobile=c,Salary=d,Location=e)
        obj.save()
        return redirect('employee_page')

def edit_employee(request,emp_id):
    data=EmployeeDb.objects.get(id=emp_id)
    return render(request,"Edit_Employee.html",{'data':data})
def update_employee(request,emp_id):
    if request.method=="POST":
        a = request.POST.get('emp_name')
        b = request.POST.get('emp_email')
        c = request.POST.get('emp_mobile')
        d = request.POST.get('emp_salary')
        e = request.POST.get('emp_place')
        EmployeeDb.objects.filter(id=emp_id).update(Name=a,Email=b,Mobile=c,Salary=d,Location=e)

        return redirect('display_employee')
def delete_employee(request,emp_id):
    x=EmployeeDb.objects.filter(id=emp_id)
    x.delete()
    return redirect('display_employee')

def register_page(request):
    return render(request,'Register.html')

def registration_data(request):
    if request.method=="POST":
        f = request.POST.get('employee_name')
        g = request.POST.get('place_name')
        h = request.POST.get('mobile_no')
        img = request.FILES['image']
        obj=Registration_Db(Name=f,Place=g,Mobile=h,ProfileImage=img)
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
        f = request.POST.get('employee_name')
        g = request.POST.get('place_name')
        h = request.POST.get('mobile_no')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Registration_Db.objects.get(id=emp_id).ProfileImage
        Registration_Db.objects.filter(id=emp_id).update(Name=f, Place=g, Mobile=h, ProfileImage=file)
        return redirect('display_registration')
def delete_registration(request,emp_id):
    x=Registration_Db.objects.filter(id=emp_id)
    x.delete()
    return redirect('display_registration')



# Create your views here.
