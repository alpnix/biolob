from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=120, default="You")
    sender = models.CharField(max_length=6, default="BioBot")

    def __str__(self): 
        return self.content

    class Meta:
        ordering = ('date',)

