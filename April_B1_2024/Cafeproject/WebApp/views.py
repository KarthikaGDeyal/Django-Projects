from django.shortcuts import render,redirect,get_object_or_404
from WebApp.models import ContactDb,RegisterDb,ClassRegistrationDb,TeamDb,TestimonialDb,CartDb,OrderDb,AboutDb,WishlistDb,ContactInfoDb,FooterDb
from CafeApp.models import DemoDb,ProDb,ClasslistDb
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
import razorpay
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def homepage(request):
    cat = DemoDb.objects.all()
    about=AboutDb.objects.all()
    hero_images = {category: category.CategoryImage.url if category.CategoryImage else '' for category in cat}
    team = TeamDb.objects.all()
    testimonials = TestimonialDb.objects.all()
    contacts = ContactInfoDb.objects.all()
    footers = FooterDb.objects.all()
    # Initialize products for different categories
    cheesecakes = ProDb.objects.filter(CategoryName="Cheesecakes")[:1]
    brownies = ProDb.objects.filter(CategoryName="Brownies")[:1]
    cinnamonrolls = ProDb.objects.filter(CategoryName="Cinnamon Rolls")[:1]
    donuts = ProDb.objects.filter(CategoryName="Donuts")[:1]
    cookies = ProDb.objects.filter(CategoryName="Cookies")[:1]
    pastries = ProDb.objects.filter(CategoryName="Pastries")[:1]
    cupcakes = ProDb.objects.filter(CategoryName="Cupcakes")[:1]
    cakes = ProDb.objects.filter(CategoryName="Cakes")[:1]
    product = ProDb.objects.all()  # Get all products by default


    return render(request, "Home.html", {
        'about':about,
        'footers':footers,
        'contacts':contacts,
        'product': product,
        'cat': cat,
        'hero_images': hero_images,
        'cakes': cakes,
        'cupcakes': cupcakes,
        'pastries': pastries,
        'cookies': cookies,
        'cheesecakes': cheesecakes,
        'brownies': brownies,
        'cinnamonrolls': cinnamonrolls,
        'donuts': donuts,
        'team': team,
        'testimonials': testimonials,
        'rating_range': range(1, 6)
    })


def aboutpage(request):
    cat = DemoDb.objects.all()
    about = AboutDb.objects.all()
    team = TeamDb.objects.all()
    footers = FooterDb.objects.all()
    testimonials = TestimonialDb.objects.all()
    return render(request,"About.html",{'about':about,'footers':footers,'cat': cat,'testimonials':testimonials,'team':team})

def Contactpage(request):
    cat = DemoDb.objects.all()
    footers = FooterDb.objects.all()
    contacts = ContactInfoDb.objects.all()
    return render(request,"Contact.html",{'cat': cat,'contacts': contacts,'footers':footers})

def save_contact(request):
    if request.method=="POST":
        a= request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('message')
        obj=ContactDb(Name=a,Email=b,Message=c)
        obj.save()
        return redirect(Contactpage)

def Classpage(request):
    cat = DemoDb.objects.all()
    footers = FooterDb.objects.all()
    return render(request,"Class.html",{'footers':footers,'cat': cat})

def Teampage(request):
    cat = DemoDb.objects.all()
    footers = FooterDb.objects.all()
    return render(request,"Team.html",{'footers':footers,'cat': cat})

def save_class(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('phone')
        c = request.POST.get('studclass')
        f = request.POST.get('req')
        obj=ClassRegistrationDb(Name=a,Phone=b,StudyingClass=c,Requirements=f)
        obj.save()
        return redirect(homepage)

def save_team(request):
    if request.method=="POST":
        a = request.FILES.get('pro')
        b = request.POST.get('name')
        c = request.POST.get('gender')
        d = request.POST.get('email')
        e = request.POST.get('mobile')
        f = request.POST.get('position')
        g = request.FILES.get('res')
        obj=TeamDb(ProfileImage=a,Name=b,Gender=c,Email=d,Mobile=e,Position=f,Resume=g)
        obj.save()
        return redirect(Teampage)

def all_products(request):
    # Retrieve all categories and products
    cat = DemoDb.objects.all()
    product = ProDb.objects.all()
    footers = FooterDb.objects.all()

    # Get selected category, search query, and sort options from the request
    selected_category = request.GET.get('cat_name')
    search_query = request.GET.get('search')
    sort_option = request.GET.get('sort')

    # Filter products by selected category first
    if selected_category:
        product = product.filter(CategoryName__iexact=selected_category)

    # Apply search filter if a search query is present
    if search_query:
        product = product.filter(ProductName__icontains=search_query)
        product = product.filter(
            Q(ProductName__icontains=search_query) |
            Q(CategoryName__icontains=search_query)
        )



    # Apply sorting based on the selected option
    if sort_option == 'price_asc':
        product = product.order_by('Price')  # Ascending order by Price
    elif sort_option == 'price_desc':
        product = product.order_by('-Price')  # Descending order by Price
    elif sort_option == 'category':
        product = product.order_by('CategoryName')  # Sort by CategoryName

    # Render the template with filtered and sorted products
    return render(request, "All_Products.html", {
        'footers':footers,
        'product': product,
        'sort_option': sort_option,
        'search_query': search_query,
        'cat': cat,
        'selected_category': selected_category  # Pass selected_category back to the template
    })



# views.py
def filtered_products(req, cat_name):
    # Get all categories and products
    cat = DemoDb.objects.all()
    footers = FooterDb.objects.all()
    # Filter products by the specified category name
    data = ProDb.objects.filter(CategoryName__iexact=cat_name)
    selected_category = req.GET.get('cat_name')
    # Check if there are additional filters like search, category, or sorting options
    search_query = req.GET.get('search')
    sort_option = req.GET.get('sort')

    # Apply search filter if a query is present
    if selected_category:
        data = data.filter(CategoryName__iexact=selected_category)
    if search_query:
        data = data.filter(ProductName__icontains=search_query)

    # Apply sorting options on the filtered data
    if sort_option == 'price_asc':
        data = data.order_by('Price')  # Ascending order by Price
    elif sort_option == 'price_desc':
        data = data.order_by('-Price')  # Descending order by Price
    elif sort_option == 'category':
        data = data.order_by('CategoryName')  # Order by CategoryName

    # Render the filtered and sorted products in the template
    return render(req, 'FilteredProducts.html', {
        'footers': footers,
        'sort_option': sort_option,
        'search_query': search_query,
        'product': data,  # Use data here, which is the filtered and sorted queryset
        'data': data,
        'datas': data,
        'cat': cat,
        'cat_name': cat_name  # Pass cat_name back to the template context
    })




def single_product(request, pro_id):
    cat = DemoDb.objects.all()
    product = get_object_or_404(ProDb, id=pro_id)
    footers = FooterDb.objects.all()
    CategoryName = product.CategoryName
    related_products = ProDb.objects.filter(CategoryName=CategoryName).exclude(id=pro_id)
    return render(request, 'SingleProduct.html', {'footers':footers,'cat':cat,'product': product,'CategoryName': CategoryName,'products':related_products })


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
        return redirect(loginpage)
def loginpage(request):
    return render(request,"Login.html")

def Userlogin(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pwd=request.POST.get('password')
        if RegisterDb.objects.filter(Name=un,Password=pwd).exists():
            request.session['Username'] = un
            request.session['Password'] = pwd
            return redirect(homepage)
        else:
            return redirect(loginpage)
    else:
        return redirect(loginpage)


def User_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(homepage)

def testimonials(request):
    testimonials = TestimonialDb.objects.all()
    footers = FooterDb.objects.all()
    cat = DemoDb.objects.all()

    return render(request, 'testimonials.html', {'footers':footers,'cat':cat,'testimonials': testimonials,'rating_range': range(1, 6)})


# views.py



def save_testimonial(request):
    if request.method == 'POST':
        a = request.FILES.get('profile')
        b = request.POST.get('names')
        c = request.POST.get('genders')
        d = request.POST.get('emails')
        e = request.POST.get('contact')
        f = request.POST.get('places')
        g = request.POST.get('review')
        h = request.POST.get('rating')  # Retrieve the rating value from the form

        # Save the data to the database
        obj = TestimonialDb(ProfileImage=a, Name=b, Gender=c, Email=d, Mobile=e, Place=f, Review=g,Rating=h)
        obj.save()



    return redirect(testimonials)

def category_detail(request, id):
    category = get_object_or_404(DemoDb, id=id)
    return render(request, 'view_details.html', {'category': category})



def product_list(request):
    # Retrieve all categories
    categories = DemoDb.objects.all()

    context = {
        'categories': categories,  # Pass categories to context
    }
    return render(request, 'FilteredProducts.html', context)

# views.py
def cart_page(request):
    # Retrieve all categories for display
    cat = DemoDb.objects.all()

    # Retrieve cart items for the logged-in user
    data = CartDb.objects.filter(Username=request.session.get('Username', ''))
    footers = FooterDb.objects.all()

    # Initialize variables for calculations
    sub_total = sum(item.Total_price for item in data)  # Calculate subtotal

    # Retrieve discount from the POST request if a discount code is provided
    discount_code = request.POST.get('discount_code', '')
    discount_percentage = get_discount_percentage(discount_code)

    # Apply discount logic
    if discount_percentage:
        discount = sub_total * discount_percentage  # Calculate discount based on subtotal
        request.session['discount_amount'] = discount  # Store discount in the session
    else:
        discount = request.session.get('discount_amount', 0)  # Retrieve from session if no new code

    # Calculate shipping cost based on subtotal
    shipping = 50 if sub_total > 700 else 100

    # Calculate the total amount after applying discount
    total = sub_total + shipping - discount

    # If there are no items in the cart, reset the fields to zero
    if not data.exists():
        sub_total = 0
        discount = 0
        shipping = 0
        total = 0
        request.session['discount_amount'] = 0  # Reset session discount

    # Prepare messages for the user regarding discount
    messages = []
    if discount > 0:
        messages.append(f"Discount applied: ₹{discount:.2f}")

    # Render the cart page with all necessary data
    return render(request, "Cart.html", {
        'footers': footers,
        'data': data,
        'discount_amount': discount,  # Pass discount amount to the template
        'cat': cat,
        'sub_total': sub_total,
        'shipping': shipping,
        'total': total,
        'messages': messages  # Include messages for display in the template
    })


def get_discount_percentage(discount_code):
    # Define your discount codes and their corresponding discounts
    discount_codes = {
        'DISCOUNT20': 0.20,  # 20% discount
        'DISCOUNT10': 0.10   # 10% discount
    }

    # Return the discount percentage if the code is valid, otherwise return None
    return discount_codes.get(discount_code.upper())


def checkout_page(request):
    cat = DemoDb.objects.all()
    data = CartDb.objects.filter(Username=request.session['Username'])
    footers = FooterDb.objects.all()

    sub_total = 0
    shipping = 0
    total = 0

    # Retrieve discount amount from session (calculated in cart_page)
    discount = request.session.get('discount_amount', 0)

    for item in data:
        sub_total += item.Total_price

    # Calculate shipping cost based on subtotal
    if sub_total > 700:
        shipping = 50  # Lower shipping cost for higher subtotal
    else:
        shipping = 100

    # Calculate the total amount after applying discount
    total = sub_total + shipping - discount

    if not data.exists():
        sub_total = 0
        discount = 0
        shipping = 0
        total = 0
        request.session['discount_amount'] = 0  # Reset session discount

    return render(request, "Checkout.html", {
        'footers': footers,
        'discount_amount': discount,  # Pass discount amount to the template
        'cat': cat,
        'data': data,
        'sub_total': sub_total,
        'shipping': shipping,
        'total': total
    })



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
        return redirect(homepage)

def delete_cart(request,data_id):
    username = request.session.get('Username')
    x=CartDb.objects.filter(Username=username,id=data_id)
    x.delete()
    messages.success(request,"Item deleted..!!")
    return redirect('cart_page')





def orderpage(request):
    customer = OrderDb.objects.order_by('-id').first()
    payy = customer.Total_price
    amount = int(payy * 100)
    payy_str = str(amount)

    for i in payy_str:
        print(i)

        if request.method == "POST":
            order_currency = 'INR'
            client = razorpay.Client(auth=('rzp_test_F4HEc8QkaBMTNE', '7Ks4vwQ1PHqg5tk9hindId6k'))
            payment = client.order.create({'amount': amount, 'currency': order_currency})

    return render(request, "Payment.html", {'customer': customer, 'payy_str': payy_str})

def save_order(request):
    if request.method == 'POST':
        a = request.POST.get('user')
        b = request.POST.get('country')
        c = request.POST.get('address')
        d = request.POST.get('town')
        e = request.POST.get('state')
        f = request.POST.get('post')
        g = request.POST.get('phone')
        h = request.POST.get('email')
        i = request.POST.get('total')
        j = request.POST.get('order')

        obj = OrderDb(Username=a, Country=b, Address=c, Town_City=d, State=e, PostCode_ZIP=f, Phone=g,Email=h,Total_price=i,Order_notes=j,payment_status='Pending')
        obj.save()
        return redirect(orderpage)

def wishlist(request):
    datas = WishlistDb.objects.all()
    cat = DemoDb.objects.all()
    footers = FooterDb.objects.all()
    data = WishlistDb.objects.filter(Username=request.session['Username'])
    return render(request, 'Wishlist.html', {'footers':footers,'cat':cat,'data':data,'datas':datas})

def save_wishlist(request):
    if request.method == 'POST':
        b = request.POST.get('pro_name')
        c = request.POST.get('price')
        d = request.POST.get('in_stock')

        if request.session.get('Username'):
            obj = WishlistDb(Username=request.session.get('Username'), ProductName=b, Price=c, Stock=d)
            obj.save()
            messages.success(request, "Added to Wishlist")
        else:
            messages.error(request, "User is not logged in. Cannot add to wishlist.")
        return redirect(wishlist)


def delete_item(request, item_id):
    # Find the item by ID and delete it
    wishlist_item = WishlistDb.objects.get(id=item_id)
    wishlist_item.delete()
    return redirect('wishlist')  # Redirect back to the wishlist view


def save_cart_wishlist(request):
    if request.method == 'POST':
        # Retrieve the product ID from the hidden input field
        pro_id = request.POST.get('pro_id')

        # Check if the product ID is valid
        if pro_id:
            try:
                # Get the product from the wishlist using the provided ID
                wishlist_item = WishlistDb.objects.get(id=pro_id)

                # Create a new entry in the CartDb table using the wishlist item details
                cart_item = CartDb(
                    Username=wishlist_item.Username,
                    Product_name=wishlist_item.ProductName,
                    Price=wishlist_item.Price,
                    Quantity=1,  # Set a default quantity for the cart
                    Total_price=wishlist_item.Price * 1,  # Calculate total price based on quantity
                )
                cart_item.save()

                # Remove the item from the wishlist after adding it to the cart
                wishlist_item.delete()

                # Display a success message
                messages.success(request, f"{wishlist_item.ProductName} added to cart!")

                # Redirect the user to the cart page or wishlist page
                return redirect('wishlist')  # Change 'wishlist' to 'cart' if needed

            except WishlistDb.DoesNotExist:
                # If the product does not exist in the wishlist, show an error message
                messages.error(request, "The product could not be found in your wishlist.")
                return redirect('wishlist')

    # Redirect to wishlist if the method is not POST
    return redirect('cart_page')


# Sample discounts based on conditions

def apply_discount(request):
    # Check if the request method is POST
    if request.method == 'POST':
        discount_code = request.POST.get('coupon_code')

        # Retrieve the logged-in user's username from session
        username = request.session.get('Username')

        # If the user is not logged in, redirect them to the login page
        if not username:
            messages.error(request, "You need to be logged in to apply a discount.")
            return redirect('loginpage')

        # Fetch the user's cart items from the database
        cart_items = CartDb.objects.filter(Username=username)

        # Calculate the subtotal
        sub_total = sum(item.Total_price for item in cart_items)

        # Initialize discount variables
        discount = 0

        # Check if the discount code is valid (assuming DISCOUNTS is a predefined dictionary)
        DISCOUNTS = {
            'DISCOUNT10': (0.10, 500),  # 10% off, Minimum amount 500
            'SAVE20': (0.20, 700),      # 20% off, Minimum amount 700
        }

        # Validate the discount code and calculate new total
        if discount_code in DISCOUNTS:
            discount_percentage, min_amount = DISCOUNTS[discount_code]

            # Check if the subtotal meets the minimum amount required for the discount
            if sub_total >= min_amount:
                discount = sub_total * discount_percentage  # Calculate discount amount
                new_total = sub_total - discount  # Calculate new total after discount

                # Show a success message
                messages.success(request, f"{int(discount_percentage * 100)}% discount applied! Your new total is ₹{new_total:.2f}")
            else:
                # If the subtotal is not enough for the discount
                messages.error(request, f"This discount is not applicable for your total amount of ₹{sub_total:.2f}. Minimum required is ₹{min_amount:.2f}.")
                new_total = sub_total  # No discount applied
        else:
            # Invalid discount code entered
            messages.error(request, "Invalid discount code")
            new_total = sub_total  # No discount applied

        # Calculate shipping cost based on subtotal
        shipping = 50 if sub_total > 700 else 100  # Example shipping logic
        final_total = new_total + shipping# Final total after applying shipping

        # Store the discount and final total in the session
        request.session['discount_amount'] = discount
        request.session['new_total'] = final_total

    else:
        # For GET requests, redirect to the cart page
        return redirect('cart_page')

    # Redirect to cart page with updated total
    return redirect('cart_page')




def class_list_view(request):
    # Retrieve all class items from the database
    cat = DemoDb.objects.all()
    footers = FooterDb.objects.all()
    classes = ClasslistDb.objects.all()
    return render(request, 'Class.html', {'cat':cat,'footers':footers,'classes': classes})



def payment_success(request):
    # Retrieve the logged-in user's username from session
    username = request.session.get('Username')

    # Check if the user is logged in
    if not username:
        messages.error(request, "You need to be logged in to complete the payment.")
        return redirect('loginpage')

    # Update the order status to 'Completed'
    order_id = request.POST.get('order_id')  # Assuming order_id is passed in the POST request
    OrderDb.objects.filter(payment_status__isnull=True).update(payment_status='Pending')

    # Delete all items from the cart for the logged-in user
    CartDb.objects.filter(Username=username).delete()

    # Clear the session values related to the cart
    if 'discount_amount' in request.session:
        del request.session['discount_amount']
    if 'new_total' in request.session:
        del request.session['new_total']

    # Display a success message
    messages.success(request, "Payment successful! Your cart has been cleared and order confirmed.")

    # Redirect to the homepage or confirmation page
    return redirect('homepage')  # Replace 'homepage' with your desired redirect view

def chatpage(request):
    footers = FooterDb.objects.all()
    return render(request, 'ChatBot.html', {'footers':footers})








































