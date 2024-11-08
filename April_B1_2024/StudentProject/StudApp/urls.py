from django.urls import path
from StudApp import views
urlpatterns=[
    path('Student_page/',views.Student_page,name="Student_page")
]