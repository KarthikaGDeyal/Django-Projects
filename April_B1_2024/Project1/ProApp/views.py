from django.shortcuts import render, redirect
from ProApp.models import Registration
def Studentpage(request):
    return render(request,"Project.html")
def save_student(request):
    if request.method =="POST":
        a = request.POST.get('stud_name')
        b = request.POST.get('stud_place')
        c = request.POST.get('stud_course')
        obj = Registration(Name=a,Place=b,Course=c)
        obj.save()
        return redirect(Studentpage)

# Create your views here.
