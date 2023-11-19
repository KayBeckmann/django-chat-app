from django.shortcuts import render

# Create your views here.
def index(request):
  if request.method == 'POST':
    print("Received data: " + request.POST['message'])
  return render(request, 'chat/index.html', {'username':'Kay'})