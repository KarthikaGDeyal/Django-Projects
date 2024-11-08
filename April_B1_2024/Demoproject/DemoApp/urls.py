from django.urls import path
from DemoApp import views
urlpatterns=[
    path('Employee_page/',views.Employee_page,name="Employee_page")
]