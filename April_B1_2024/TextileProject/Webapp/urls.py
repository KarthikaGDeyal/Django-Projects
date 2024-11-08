from django.urls import path
from Webapp import views
urlpatterns=[
path('Homepage/',views.Homepage,name="Homepage"),
path('Aboutpage/',views.Aboutpage,name="Aboutpage"),
path('Contactpage/',views.Contactpage,name="Contactpage"),
path('save_contact/',views.save_contact,name="save_contact"),
path('all_products/',views.all_products,name="all_products"),
path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
path('filtered_products/<cat_name>',views.filtered_products,name="filtered_products"),
path('registration/',views.registration,name="registration"),
path('save_registration/',views.save_registration,name="save_registration"),
path('save_cart/',views.save_cart,name="save_cart"),
path('cart_page/',views.cart_page,name="cart_page"),
path('checkout_page/',views.checkout_page,name="checkout_page"),
path('delete_item/<int:dataid>/',views.delete_item,name="delete_item"),
path('',views.loginpage,name="loginpage"),
path('Userlogin/',views.Userlogin,name="Userlogin"),
path('User_logout/',views.User_logout,name="User_logout"),
path('orderpage/',views.orderpage,name="orderpage"),
path('save_order/',views.save_order,name="save_order"),
]