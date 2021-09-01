from django.urls import path

from . import views

app_name="chatbot"
urlpatterns = [
    path("chatbot/", views.index, name="index"),
    path("<str:product>/coming-soon/", views.coming_soon, name="coming_soon"),
    path("chatbot/clear/", views.clear_chat, name="clear"),
]