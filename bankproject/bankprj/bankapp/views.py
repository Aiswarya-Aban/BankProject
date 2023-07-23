from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bankapp.models import Forms

from bankapp.models import Forms


# Create your views here.

def home(request):
   return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,"login.html")

def newpage(request):
    return render(request, 'newpage.html')

def forms(request):
    if request.method=='POST':
        uname = request.POST['uname']
        dob=request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phn = request.POST['phn']
        mail = request.POST['mail']
        address = request.POST['address']
        dist = request.POST['dist']
        branch = request.POST['branch']
        acc=request.POST['acc']
        debit = request.POST.get('debitCheckbox', '')
        credit = request.POST.get('creditCheckbox', '')
        cheque = request.POST.get('chequeCheckbox', '')
        material = f"{debit}, {credit}, {cheque}"
        user = request.user.username

        form = Forms()
        form.uname = user
        form.dob = dob
        form.age = age
        form.gender = gender
        form.phn = phn
        form.mail = mail
        form.dist = dist
        form.branch = branch
        form.acc = True
        form.save()
        return redirect('/')
    # else:
    #     return redirect('forms')
    return render(request,'forms.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password)
                 user.save();
                 return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')