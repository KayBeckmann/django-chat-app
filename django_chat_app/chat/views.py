from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .models import Chat

# Create your views here.
@login_required(login_url='/login/')
def index(request):
  if request.method == 'POST':
    myChat = Chat.objects.get(id=1)
    print("Received data: " + request.POST['message'])
    Message.objects.create(text=request.POST['message'], author=request.user, receiver=request.user, chat=myChat)
  
  chatMessages = Message.objects.filter(chat__id=1)

  if request.user.is_authenticated:
    return render(request, 'chat/index.html', {'messages': chatMessages})
  else:
    return render(request, 'chat/error.html')
  

def loginView(request):
  redirect = request.GET.get('next')

  if request.method == 'POST':
    user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
    
    if user:
      login(request, user)
      return HttpResponseRedirect('/chat/')
    else:
      return render(request, 'chat/login.html', {'error': True, 'redirect': redirect})

  return render(request, 'chat/login.html', {'redirect': redirect})

def registerView(request):
  if request.method == 'POST':
    user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
    login(request, user)
    return HttpResponseRedirect('/chat/')

  return render(request, 'chat/register.html')