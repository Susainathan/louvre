from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import registerForm
from .models import Registeron
from .forms import signinForm
from .forms import ticketForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def home(request):
    return render(request,'index.html')

def visit(request):
    return render(request,'visit.html')

def explore(request):
    return render(request,'Explore.html')

def visitor(request):
    return render(request,'Visitor.html')

def contactus(request):
    return render(request,'contact.html')

def signin(request):
    if request.method=="POST":
        try:
            Userdetails=Registeron.objects.get(Username=request.POST['Username'],Password=request.POST['Password'])
            print("Username=",Userdetails)
            request.session['Username']=Userdetails.Username
            return redirect('ticket')
        except:
            messages.error(request,'Invalid credentials')
    form = signinForm()
    return render(request,'signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request,'You have loged out successfully')
    return redirect('signin')

def regist(request):
    if request.method=='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User has been registered!!!')
            return redirect('signin')
        return redirect('regist')
    else:
        form=registerForm()
    con={'form':form}
    return render(request,'Register.html',con)

def ticket(request):
    if request.method=='POST':
        form=ticketForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,'Welcome to Louvre you have booked the ticked successfully. You can collect the ticket when you visit Louvre.We would be delighted to help you.')
            return redirect('ticket')
        return redirect('ticket')
    else:
        form=ticketForm()
    tick={'form':form}
    return render(request, 'Ticket.html',tick)

def whatson(request):
    return render(request,'after.html')