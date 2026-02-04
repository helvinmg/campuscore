from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pagesapp/home.html')
def contact(request):
    return render(request,'pagesapp/contact.html')
def about(request):
    return render(request,'pagesapp/about.html')