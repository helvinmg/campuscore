from django.urls import path
from . import views
urlpatterns = [
    path('list',views.student_list),#students/list
    path('form',views.student_form)#students/form
]