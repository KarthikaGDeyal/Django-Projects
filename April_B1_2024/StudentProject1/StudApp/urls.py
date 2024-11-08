from django.urls import path
from StudApp import views
urlpatterns=[
path('Studentpage/', views.Studentpage,name="Studentpage"),
path('save_student/',views.save_student,name="save_student")
]