from django.urls import path
from TextApp import views
urlpatterns=[
path('index_page/',views.index_page,name="index_page"),
path('demo_page/',views.demo_page,name="demo_page"),
path('save_demo/',views.save_demo,name="save_demo"),
path('view_details/',views.view_details,name="view_details"),
path('edit_details/<int:cat_id>/',views.edit_details,name="edit_details"),
path('update_details/<int:cat_id>/',views.update_details,name="update_details"),
path('delete_details/<int:cat_id>/',views.delete_details,name="delete_details"),
path('product_page/',views.product_page,name="product_page"),
path('save_product/',views.save_product,name="save_product"),
path('product_details/',views.product_details,name="product_details"),
path('edit_product/<int:pro_id>/',views.edit_product,name="edit_product"),
path('update_product/<int:pro_id>/',views.update_product,name="update_product"),
path('delete_product/<int:pro_id>/',views.delete_product,name="delete_product"),
path('admin_page/',views.admin_page,name="admin_page"),
path('admin_login/',views.admin_login,name="admin_login"),
path('admin_logout/',views.admin_logout,name="admin_logout"),
path('contact_page/',views.contact_page,name="contact_page"),
path('delete_contact/<int:co_id>',views.delete_contact,name="delete_contact"),
path('register_page/',views.register_page,name="register_page"),
path('delete_registration/<int:re_id>',views.delete_registration,name="delete_registration"),





]