from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode

from . import chatbot
from .models import Message
# Create your views here.


@login_required(login_url="home:login")
def index(request):
    context = {
        "messages": Message.objects.filter(username=request.user), 
    }

    if request.method == "POST":
      content = request.POST["content"]

      if not content: 
        error = f"""
            <div class="message">
              <p class="meta">BioBot <span><span/></p>
              <p class="text text-danger">
                You should write a message before you send!!
              </p>
            </div>"""
        return HttpResponse(error)

      user = request.user
      m = Message(content=content, username=user, sender="You")
      m.save()

      message = f"""
        <div class="message">
          <p class="meta">You <span>{m.date.strftime("%b. %d, %H:%M")}</span></p>
          <p class="text">
            {m.content}
          </p>
        </div>"""
      r = Message(content=chatbot.generate_response(m.content), username=user, sender="BioBot")
      r.save()

      response = f"""
        <div class="message">
          <p class="meta">BioBot <span>{r.date.strftime("%b. %d, %H:%M")}</span></p>
          <p class="text">
            {r.content}
          </p>
        </div>"""
      return HttpResponse(message + response)

    return render(request, "chatbot/index.html", context)

def coming_soon(request, product):
    context = {"html": "base.html"}
    if request.user.is_authenticated:
        context["html"] = "auth_base.html"
    
    return render(request, "main/coming_soon.html", context)

def clear_chat(request):
    for message in Message.objects.filter(username=request.user):
        message.delete()

    return redirect("chatbot:index")

