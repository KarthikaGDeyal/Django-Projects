from django.urls import path
from DepApp import views
urlpatterns=[
    path('Department_page/',views.Department_page,name="Department_page")
]