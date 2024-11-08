from django.urls import path
from Newapp import views
urlpatterns=[
    path('Register_page/',views.Register_page,name="Register_page")

]