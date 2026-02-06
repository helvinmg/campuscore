from django.urls import path
from . import views
urlpatterns = [
    path('list',views.student_list,name="studentlist"),#students/list
    path('form',views.student_form),#students/form
    path('delete/<int:sid>',views.student_delete),
    path('update/<int:sid>',views.student_update),
]