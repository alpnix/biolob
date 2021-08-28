from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Message
# Create your views here.


@login_required(login_url="home:login")
def index(request):
    context = {
        "messages": Message.objects.filter(username=request.user)
    }
    if request.method == "POST":
        from . import chatbot
        print(request.POST)
        content = request.POST["content"]
        if not content: 
            return render(request, "main/coming_soon.html", context)
        user = request.user
        m = Message(content=content, username=user)
        m.save()

        message = f"""
        <div class="message">
          <p class="meta">You <span>{m.date.strftime("%b. %d, %H:%M")}</span></p>
          <p class="text">
            {m.content}
          </p>
        </div>"""
        response = f"""
                <div class="message">
          <p class="meta">You <span>{m.date.strftime("%b. %d, %H:%M")}</span></p>
          <p class="text">
            {chatbot.generate_response(m.content)}
          </p>
        """
        return HttpResponse(message + response)

    return render(request, "chatbot/index.html", context)

def coming_soon(request, product):
    context = {"html": "base.html"}
    if request.user.is_authenticated:
        context["html"] = "auth_base.html"
    
    return render(request, "main/coming_soon.html", context)
