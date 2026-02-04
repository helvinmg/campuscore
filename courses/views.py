from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course_catalog (request):
    courses=['Btech CSE','Btech ECE','Btech ME','Btech CE','Btech EE','Mtech Cyber Security','Mtech Embedded Systems']
    count={"UG":4,"PG":2}
    return render(request,'courses/course_catalog.html',{'courses':courses,'count':count})