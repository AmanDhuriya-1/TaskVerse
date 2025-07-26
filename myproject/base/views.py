from django.shortcuts import render,redirect
from base.models import TaskModel

# Create your views here.


def home(request):


    return render(request,'home.html')

def add(request):

    if request.method=='POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']
        TaskModel.objects.create(title=title_data,desc=desc_data)
        return redirect('home')

    return render(request,'add.html')