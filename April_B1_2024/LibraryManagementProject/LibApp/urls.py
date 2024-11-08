from django.urls import path
from LibApp import views
urlpatterns=[
path('Library_page/',views.Library_page,name="Library_page"),
path('student_page/',views.student_page,name="student_page"),
path('display_student/',views.display_student,name="display_student"),
path('save_student/',views.save_student,name="save_student"),
path('Add_Book/',views.Add_Book,name="Add_Book"),
path('Book_page/',views.Book_page,name="Book_page"),
path('display_book/',views.display_book,name="display_book"),
path('edit_student/<int:stud_id>/',views.edit_student,name="edit_student"),
path('update_student/<int:stud_id>/',views.update_student,name="update_student"),
path('edit_book/<int:book_id>/',views.edit_book,name="edit_book"),
path('delete_student/<int:stud_id>/',views.delete_student,name="delete_student"),
path('update_book/<int:book_id>/',views.update_book,name="update_book")

]