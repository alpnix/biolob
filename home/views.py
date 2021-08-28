from django.shortcuts import render, redirect
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from chatbot.models import Message

# Create your views here.

def index(request):
    context = {
        "username": request.user,
    }
    if request.user.is_authenticated:
        return render(request, "main/auth_index.html", context)
    else:
        return render(request, "main/index.html", context)
        

def dashboard(request):
    context = {}

    if request.method == "POST": 
        context["username"] = request.POST["username"]
        return render(request, "main/auth_index.html", context)

    return render(request, "main/auth_index.html", context)


def loginPage(request):
    context = {}
    if request.method == "POST": 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home:index")
        else: 
            messages.info(request, "Username OR password is incorrect!")
            
    return render(request, "auth/login.html", context)

def logoutPage(request):
    for message in Message.objects.filter(username=request.user):
        message.delete()

    logout(request)
    return redirect("home:index")


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home:index")

    form = CreateUserForm()
    if request.method == "POST": 
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data["username"]
            messages.success(request, "Account successfully created for " + user)
            return redirect("home:login")

    context = {"form": form}    
    return render(request, "auth/register.html", context)
