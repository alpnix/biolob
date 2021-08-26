from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="home:login")
def index(request):
    context = {}
    return render(request, "chatbot/index.html", context)