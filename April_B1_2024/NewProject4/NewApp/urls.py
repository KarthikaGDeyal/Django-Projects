from django.urls import path
from NewApp import views
urlpatterns=[
    path('index_page/',views.index_page,name="index_page")
]