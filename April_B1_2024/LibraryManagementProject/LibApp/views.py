from django.shortcuts import render, redirect
from LibApp.models import StudentDb, BookDb
def Library_page(request):
    return render(request, 'index.html')
# Create your views here.
def student_page(req):
    return render(req,'Add_Student.html')
def display_student(request):
    data = StudentDb.objects.all()
    return render(request, "Display_Student.html", {'data': data})

def save_student(request):
    if request.method=="POST":
        a= request.POST.get('stud_name')
        b = request.POST.get('stud_age')
        c = request.POST.get('stud_mobile')
        d = request.POST.get('stud_email')
        e = request.POST.get('stud_address')
        f = request.POST.get('stud_course')
        h = request.POST.get('stud_gender')
        obj=StudentDb(Name=a,Age=b,Mobile=c,Email=d,Address=e,Course=f,Gender=h)
        obj.save()
        return redirect('student_page')
def Add_Book(request):
    return render(request, "Add_Book.html")


def Book_page(request):
    if request.method == "POST":
        i = request.POST.get('book_name')
        j = request.POST.get('author_name')
        k = request.POST.get('book_price')
        l = request.POST.get('book_date')
        obj = BookDb(BookName=i, AuthorName=j, Price=k, PublishedDate=l)
        obj.save()
        return redirect('Add_Book')
def display_book(request):
    data = BookDb.objects.all()
    return render(request, "Display_book.html", {'data': data})
def edit_student(request,stud_id):
    data=StudentDb.objects.get(id=stud_id)
    return render(request,"Edit_Student.html",{'data':data})
def update_student(request,stud_id):
    if request.method=="POST":
        a = request.POST.get('stud_name')
        b = request.POST.get('stud_age')
        c = request.POST.get('stud_mobile')
        d = request.POST.get('stud_email')
        e = request.POST.get('stud_address')
        f = request.POST.get('stud_course')
        h = request.POST.get('stud_gender')
        StudentDb.objects.filter(id=stud_id).update(Name=a, Age=b, Mobile=c, Email=d, Address=e, Course=f, Gender=h)

        return redirect('display_student')
def edit_book(request,book_id):
    data=BookDb.objects.get(id=book_id)
    return render(request,"Edit_Book.html",{'data':data})

def update_book(request,book_id):
    if request.method=="POST":
        i = request.POST.get('book_name')
        j = request.POST.get('author_name')
        k = request.POST.get('book_price')
        l = request.POST.get('book_date')
        BookDb.objects.filter(id=book_id).update(BookName=i, AuthorName=j, Price=k, PublishedDate=l)
        return redirect('display_book')
def delete_student(request,stud_id):
    x=StudentDb.objects.filter(id=stud_id)
    x.delete()
    return redirect('display_student')


