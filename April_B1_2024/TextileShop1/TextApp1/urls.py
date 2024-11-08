from django.urls import path
from TextApp1 import views
urlpatterns=[
path('index_page/',views.index_page,name="index_page"),
path('demo_page/',views.demo_page,name="demo_page"),
path('save_demo/',views.save_demo,name="save_demo"),
path('view_details/',views.view_details,name="view_details"),
path('edit_details/<int:cat_id>/',views.edit_details,name="edit_details"),
path('update_details/<int:cat_id>/',views.update_details,name="update_details"),
path('delete_details/<int:cat_id>/',views.delete_details,name="delete_details"),

]
