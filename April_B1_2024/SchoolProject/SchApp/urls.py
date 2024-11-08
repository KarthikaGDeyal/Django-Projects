from django.urls import path
from SchApp import views
urlpatterns=[
    path('Schoolpage/',views.Schoolpage,name="Schoolpage")
]