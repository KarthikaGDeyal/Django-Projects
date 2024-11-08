from django.urls import path
from ColApp import views
urlpatterns=[
    path('College_page/',views.College_page,name="College_page")
]