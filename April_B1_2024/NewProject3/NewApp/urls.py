from django.urls import path
from NewApp import views
urlpatterns=[
path('Registerpage/',views.Registerpage,name="Registerpage")
]