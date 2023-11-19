from django.shortcuts import render
from .models import Message
from .models import Chat

# Create your views here.
def index(request):
  if request.method == 'POST':
    myChat = Chat.objects.get(id=1)
    print("Received data: " + request.POST['message'])
    Message.objects.create(text=request.POST['message'], author=request.user, receiver=request.user, chat=myChat)
  return render(request, 'chat/index.html', {'username':'Kay'})