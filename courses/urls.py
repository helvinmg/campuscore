from django.urls import path
from . import views
urlpatterns = [
    path('catalog',views.course_catalog),
    path('details',views.course_details),
]