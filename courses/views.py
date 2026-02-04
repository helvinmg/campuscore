from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course_catalog (request):
    return render(request,'courses/course_catalog.html')