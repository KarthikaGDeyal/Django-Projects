from django.urls import path
from ShopApp import views
urlpatterns=[
path('shop_page/',views.shop_page,name="shop_page"),
path('register_page/',views.register_page,name="register_page"),
path('registration_data/',views.registration_data,name="registration_data"),
path('display_registration/',views.display_registration,name="display_registration"),
path('edit_registration/<int:emp_id>/',views.edit_registration,name="edit_registration"),
path('update_registration/<int:emp_id>/',views.update_registration,name="update_registration"),
path('delete_registration/<int:emp_id>/',views.delete_registration,name="delete_registration"),
]