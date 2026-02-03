from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_list(request):
    return render(request,'student_list.html')
    #return HttpResponse("Welcome to the Student Directory")