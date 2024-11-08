from django.urls import path
from TeachApp import views
urlpatterns=[
path('Teacherpage/',views.Teacherpage,name="Teacherpage"),
path('save_teacher/',views.save_teacher,name="save_teacher")
]