from django.shortcuts import render,redirect
from StudApp.models import StudentRegistration

# Create your views here.
def Studentpage(request):
    return render(request,"Student.html")
def save_student(request):
    if request.method=="POST":
        a= request.POST.get('stud_name')
        b = request.POST.get('stud_place')
        c = request.POST.get('stud_course')
        d = request.POST.get('stud_company')
        e = request.POST.get('stud_salary')
        f = request.POST.get('stud_mobile')
        g = request.POST.get('stud_email')
        h = request.POST.get('Address')
        i = request.POST.get('Designation')
        j = request.POST.get('Gender')
        obj=StudentRegistration(Name=a,Place=b,Course=c,Company=d,Salary=e,Mobile=f,Email=g,Address=h,Designation=i,Gender=j)
        obj.save()
        return redirect(Studentpage)
