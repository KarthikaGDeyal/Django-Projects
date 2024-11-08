from django.urls import path
from EmpApp import views
urlpatterns=[
path('index_page/',views.index_page,name="index_page"),
path('employee_page/',views.employee_page,name="employee_page"),
path('display_employee/',views.display_employee,name="display_employee"),
path('save_employee/',views.save_employee,name="save_employee"),
path('edit_employee/<int:emp_id>/',views.edit_employee,name="edit_employee"),
path('update_employee/<int:emp_id>/',views.update_employee,name="update_employee"),
path('delete_employee/<int:emp_id>/',views.delete_employee,name="delete_employee"),

path('register_page/',views.register_page,name="register_page"),
path('registration_data/',views.registration_data,name="registration_data"),
path('display_registration/',views.display_registration,name="display_registration"),
path('edit_registration/<int:emp_id>/',views.edit_registration,name="edit_registration"),
path('update_registration/<int:emp_id>/',views.update_registration,name="update_registration"),
path('delete_registration/<int:emp_id>/',views.delete_registration,name="delete_registration"),


]