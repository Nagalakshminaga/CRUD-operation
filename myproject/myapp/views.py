from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas


# Create your views here.
def home(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,'home.html',{'datas':mydata})
    else:
        return render(request,'home.html')
        
def addData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        address=request.POST.get('address') 
        contact=request.POST.get('contact')
        mail=request.POST.get('mail')
        
        Datas.objects.create(
          Name=name,
          Age=age,
          Address=address,
          Contact=contact,
          Mail=mail)
          
        return redirect('home')
    return render(request,'home.html')

def updateData(request,id):
    mydata=Datas.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        address=request.POST.get('address') 
        contact=request.POST.get('contact')
        mail=request.POST.get('mail')
        
        mydata.Name=name
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()
        return redirect('home')

    return render(request,'update.html',{'data':mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')
