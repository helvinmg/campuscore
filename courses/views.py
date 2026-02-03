from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course_catalog (request):
    return HttpResponse('Browse our available courses here')