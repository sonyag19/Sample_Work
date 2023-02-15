from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import *
from .models import *



# Create your views here.
def add(request):
    if request.method=='POST':
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        result=num1+num2
        return render(request,'sum.html',{'add': result})
    else:
        return render(request, 'addition.html')

def sub(request):
    if request.method=='POST':
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        result=num1-num2
        return render(request,'sum.html',{'sub': result})
    else:
        return render(request, 'substraction.html')

def mul(request):
    if request.method=='POST':
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        result=num1*num2
        return render(request,'sum.html',{'mul': result})
    else:
        return render(request, 'multiplication.html')

def div(request):
    if request.method=='POST':
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        result=num1/num2
        return render(request,'sum.html',{'div': result})
    else:
        return render(request, 'division.html')


def register(request):
    if request.method=='POST':
        a=regform(request.POST)             #form
        if a.is_valid():                     # to check validity
            nm=a.cleaned_data['name']           # validated data is called cleaned_data
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            cp=a.cleaned_data['confirm']
            if ps==cp:                          # for moving validated data to model
                b=regmodel(name=nm,email=em,password=ps)
                b.save()                             # to commit
                return redirect(login)
            else:
                return HttpResponse("Password doesn't match")
        else:
            return HttpResponse("Registration Failed")
    else:
        return render(request,'registration.html')


def register2(request):
    if request.method=='POST':
        a=reg2form(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            ln=a.cleaned_data['lname']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            ad=a.cleaned_data['addr']
            c=reg2model(fname=fn,lname=ln,email=em,phone=ph,addr=ad)
            c.save()
            return HttpResponse("Data Stored Successfully")
        else:
            return HttpResponse("Data Storage Failed")
    else:
        return render(request,'registration2.html')


def login(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=regmodel.objects.all()  # to take all datas from model
            for i in b:
                if em==i.email and ps==i.password:
                    return HttpResponse("Login Success")
            else:
                return HttpResponse("Login failed")
    else:
        return render(request,'login.html')


def search(request):
    if request.method=='POST':
        a=searchform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            b=reg2model.objects.all()
            for i in b:
                if nm==i.fname and em==i.email and ph==i.phone:
                    return HttpResponse("Person Found...")
            else:
                return HttpResponse("Not Found...")
    else:
        return render(request,'searchperson.html')


# database(regmodel) --> backend(python) --> template {{}}
def display(request):
    a=regmodel.objects.all()
    return render(request,'display.html',{'a':a})


def display2(request):
    a=reg2model.objects.all()
    return render(request,'display2.html',{'a':a})

# never use model & form names as function name

def file(request):
    if request.method=='POST':
        a=fileform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['iname']
            pr=a.cleaned_data['iprice']
            ds=a.cleaned_data['des']
            im=a.cleaned_data['image']
            b=filemodel(iname=nm,iprice=pr,des=ds,image=im)
            b.save()
            return HttpResponse("File Uploaded Successfully...")
        else:
            return HttpResponse("Failed")
    else:
        return render(request,'fileupload.html')

# To display image file
def filedisplay(request):
    a=filemodel.objects.all()
    li=[]
    name=[]
    dis1=[]
    price=[]
    for i in a:
        nm=i.iname
        name.append(nm)
        pri = i.iprice
        price.append(pri)
        dis=i.des
        dis1.append(dis)
        path = i.image
        li.append(str(path).split("/")[-1])
    mylist=zip(name,price,dis1,li)
    return render(request,'carddisplay.html',{'mylist':mylist})


def header(request):
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

def index(request):
    return render(request,'index.html')


def regboot(request):
    if request.method=='POST':
        a=regbootform(request.POST)             #form
        if a.is_valid():                     # to check validity
            fn=a.cleaned_data['fname']
            ln=a.cleaned_data['lname']
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            rp=a.cleaned_data['repassword']
            if ps==rp:                          # for moving validated data to model
                b=regbootmodel(fname=fn,lname=ln,email=em,password=ps,repassword=rp)
                b.save()                             # to commit
                return redirect(loginboot)
            else:
                return HttpResponse("Password doesn't match")
        else:
            return HttpResponse("Registration Failed")
    else:
        return render(request,'registration_boot.html')


def loginboot(request):
    if request.method=='POST':
        a=loginbootform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=regbootmodel.objects.all()  # to take all datas from model
            for i in b:
                if em==i.email and ps==i.password:
                    return redirect(home)
            else:
                return HttpResponse("Login failed")
    else:
        return render(request,'login_boot.html')

def home(request):
    return render(request,'home.html')

