from django.shortcuts import render
from .models import Profile,Request_To_Chat
from .models import Request_To_Chat

# Create your views here.
 
def home(request):
    context = {
        'profiles': Profile.objects.all()

    }
    
    return render(request, 'meet/home.html',context)

def about(request):
    return render(request, 'meet/about.html')

def req_to_chat(request):
    user = Request_To_Chat(name = 'sam')
    user.save()