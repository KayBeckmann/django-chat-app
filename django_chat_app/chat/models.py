from django.db import models
from django.db.models.fields import DateField
from datetime import date
from django.conf import settings

# Create your models here.
class Message(models.Model):
  text = models.CharField(max_length=512)
  created_at = DateField(default=date.today)
  # chat =chat klasse verknüpfen
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
  receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')

  def __str__(self): #Overview in adminpanel
    return f"{self.created_at}: {self.author} -> {self.text} "


class Chat(models.Model):
  created_at = DateField(default=date.today)

  def __str__(self): #Overview in adminpanel
    return f"{self.created_at}"