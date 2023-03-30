from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def find_job(request):
    return render(request,'find_job.html')
