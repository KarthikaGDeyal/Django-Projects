from django.shortcuts import render,redirect
from TeachApp.models import Registration
def Teacherpage(request):
    return render(request,"Teacher.html")
def save_teacher(request):
    if request.method=="POST":
        a=request.POST.get('tea_name')
        b = request.POST.get('tea_place')
        c = request.POST.get('tea_course')
        obj=Registration(Name=a,Place=b,Course=c)
        obj.save()
        return redirect(Teacherpage)




# Create your views here.
