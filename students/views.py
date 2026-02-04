from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_list(request):
    #data fetching data from db
    stud_records=[{'slno':1,'name':'rahul','course':'cs','sem':3},{'slno':2,'name':'reena','course':'cs','sem':3}]
    data={'admission_closed':False,"count":59,'students':stud_records}
    return render(request,'students/student_list.html',{'adm_data':data})
    #render can accept a 3rd argument in form of dictionary - context
   