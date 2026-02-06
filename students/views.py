from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
# Create your views here.
def student_list(request):
    data=Student.objects.all()#select * from Student
    print(data)#records fetched from student table
    return render(request,'students/student_list.html',{'data':data,'count':len(data)})

def student_form(request):
        #when /students/form is called by browser
        if request.method=="GET":
            form=StudentForm()
            return render(request,'students/student_form.html',{'form':form})
        else:#when form is submitted /students/form is called in POST
             form=StudentForm(request.POST)#filled form
             if form.is_valid():#checking if form valid
                  form.save()#make changes to db
             return redirect('studentlist')#redirect check for the name in urls.py
        
def student_delete(request,sid):
     record=Student.objects.get(id=sid)#select * from student where id=sid
     record.delete()
     return redirect('studentlist')
# def student_list(request):
#     #data fetching data from db
#     stud_records=[{'slno':1,'name':'rahul','course':'cs','sem':3},{'slno':2,'name':'reena','course':'cs','sem':3}]
#     data={'admission_closed':True,"count":65,'students':stud_records}
#     return render(request,'students/student_list.html',{'adm_data':data})
    #render can accept a 3rd argument in form of dictionary - context
   