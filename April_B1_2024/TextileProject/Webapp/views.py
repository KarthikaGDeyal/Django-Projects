from django.shortcuts import render,redirect
from Webapp.models import ContactDb,RegisterDb,CartDb,OrderDb
from TextApp.models import DemoDb,ProDb
from django.contrib import messages
import razorpay
def Homepage(request):
    cat=DemoDb.objects.all()
    return render(request,"Home.html",{'cat':cat})
def Aboutpage(request):
    cat = DemoDb.objects.all()
    return render(request,"About.html",{'cat':cat})

def Contactpage(request):
    cat = DemoDb.objects.all()
    return render(request,"Contact.html",{'cat':cat})

def save_contact(request):
    if request.method=="POST":
        a= request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('message')
        obj=ContactDb(Name=a,Email=b,Message=c)
        obj.save()
        return redirect(Contactpage)

def all_products(request):
    cat = DemoDb.objects.all()
    product=ProDb.objects.all()
    return render(request,"All_Products.html",{'product':product,'cat':cat})

def single_product(request,pro_id):
    cat = DemoDb.objects.all()
    product=ProDb.objects.get(id=pro_id)
    return render(request,'SingleProduct.html',{'product':product,'cat':cat})

def filtered_products(req,cat_name):
    cat = DemoDb.objects.all()
    data=ProDb.objects.filter(CategoryName=cat_name)

    return render(req,'FilteredProducts.html',{'data':data,'cat':cat})

def registration(request):
    return render(request,"Register.html")

def save_registration(request):
    if request.method=="POST":
        a= request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('password')
        d = request.POST.get('re_password')
        obj=RegisterDb(Name=a,Email=b,Password=c,ConfirmPassword=d)
        obj.save()
        messages.success(request, "Welcome..!")
        return redirect(registration)


def cart_page(request):
    cat = DemoDb.objects.all()
    data =CartDb.objects.filter(Username=request.session['Username'])
    sub_total=0
    total=0
    shipping=0
    for i in data:
        sub_total+=i.Total_price
        if sub_total>3000:
            shipping=150
        else:
            shipping=250
        total=sub_total+shipping
    return render(request,"Cart.html",{'data': data ,'cat':cat ,'sub_total':sub_total,'shipping':shipping,'total':total})

def save_cart(request):
    if request.method=="POST":
        a= request.POST.get('user')
        b = request.POST.get('name')
        c = request.POST.get('quantity')
        d = request.POST.get('price')
        e = request.POST.get('total')
        obj=CartDb(Username=a,Product_name=b,Quantity=c,Price=d,Total_price=e)
        obj.save()
        messages.success(request,"Added to cart..!!")
        return redirect(Homepage)

def delete_item(request,dataid):
    x=CartDb.objects.filter(id=dataid)
    x.delete()
    messages.success(request,"Item deleted..!!")
    return redirect(cart_page)

def checkout_page(request):
    cat = DemoDb.objects.all()
    data = CartDb.objects.filter(Username=request.session['Username'])
    sub_total = 0
    total = 0
    shipping = 0
    for i in data:
        sub_total += i.Total_price
        if sub_total > 3000:
            shipping = 150
        else:
            shipping = 250
        total = sub_total + shipping
    return render(request,"Checkout.html",{'cat':cat,'data':data,'sub_total':sub_total,'shipping':shipping,'total':total})

def loginpage(request):
    return render(request,"Login.html")

def Userlogin(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pwd=request.POST.get('password')
        if RegisterDb.objects.filter(Name=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password'] = pwd
            messages.success(request, "Welcome..!")
            return redirect(Homepage)
        else:
            messages.warning(request, "Invalid username or password")
            return redirect(loginpage)
    else:
        messages.warning(request, "User not found")
        return redirect(loginpage)

def User_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(Homepage)

def orderpage(request):
    customer=OrderDb.objects.order_by('-id').first()
    payy=customer.Total_price
    amount=int(payy*100)
    payy_str=str(amount)

    for i in payy_str:
        print(i)


    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_F4HEc8QkaBMTNE','7Ks4vwQ1PHqg5tk9hindId6k'))
        payment=client.order.create({'amount':amount,'currency':order_currency})
    return render(request, "Payment.html",{'customer':customer,'payy_str':payy_str})



def save_order(request):
    if request.method=="POST":
        a= request.POST.get('user')
        b = request.POST.get('email')
        c = request.POST.get('place')
        d = request.POST.get('address')
        e = request.POST.get('mobile')
        f = request.POST.get('message')

        h = request.POST.get('total')
        obj=OrderDb(Username=a,Email=b,Place=c,Address=d,Mobile=e,Message=f,Total_price=h)
        obj.save()
        messages.success(request,"Placed the order")
        return redirect(orderpage)







# Create your views here.
