from django.shortcuts import render
from .models import Profile,Request_To_Chat
from .models import Request_To_Chat
from django.contrib.auth.models import User

# Create your views here.
 
def home(request):
    context = {
        'profiles': Profile.objects.all()

    }
    
    return render(request, 'meet/home.html',context)

def about(request):
    return render(request, 'meet/about.html')


def req_to_chat(request):
    user1 = User.objects.get(username=request.user.username)
   
    chat = {
        'name': Request_To_Chat.objects.all(),
}
    abcd = Request_To_Chat.objects.all()
    for names in abcd:
        if names.name1 == request.POST['profile_name']  :
             return render(request,'meet/req_to_chat.html',chat)
            
    
    if request.method == 'POST' :
                s = request.POST['profile_name']
                user = User.objects.get(username=request.user.username)

                data = Request_To_Chat(name1=s, name2 = user)
                data.save()
    
    return render(request,'meet/req_to_chat.html',chat)
    
   