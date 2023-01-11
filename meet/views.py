from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Profile,Request_To_Chat
from .models import Request_To_Chat,Block,Room,Message
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView , UpdateView
from django.http import HttpResponse,JsonResponse
# Create your views here.
 
def home(request):
    context = {
        'profiles': Profile.objects.all()

    }
    
    return render(request, 'meet/home.html',context)

class ProfileListView(ListView):
    model = Profile
    template_name = 'meet/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'profiles'

class BlockView(ListView):
    model = Block
    template_name = 'meet/block.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'blocked'

    
   

class ProfileDetailView(DetailView):
    model = Profile
    
class ProfileCreateView( LoginRequiredMixin,CreateView):
    model = Profile

    fields =['likes']

    def form_valid(self,form):
        form.instance.name = self.request.user
        form.instance.username = self.request.user 
        return super().form_valid(form)

class ProfileUpdateView( LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Profile
    fields =['likes']

    def form_valid(self,form):
        form.instance.username = self.request.user 
        form.instance.name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.username:
            return True
        return False

def block_user(request):
    if request.method == 'POST' :
                s = request.POST['profile_name']
                user = User.objects.get(username=request.user.username)

                data = Block(blocked_by= user , person_blocked=s)
                data.save()
    return render(request,'meet/home.html')
    


def about(request):
    return render(request, 'meet/about.html')

def accepted(request,pk ):
    accept = Request_To_Chat.objects.get(id = pk)
    s = accept.requestor
    k = request.user.username
    if accept.is_accepted:
         return redirect('/about')

    set = Request_To_Chat.objects.all()
    for a in set:
        if a.acceptor == s and a.requestor == k:
            c = a.id
            print('heelo')
            a = Request_To_Chat.objects.get(id= c)
            a.is_accepted = False
            a.save()
    name1 = s.name + k
    ab = Room.objects.create(name= name1)
    ab.save()
    accept.is_accepted= True
    accept.save()

    return redirect('/')

def req_to_chat(request):
    user1 = User.objects.get(username=request.user.username)
   
    chat = {
        'name': Request_To_Chat.objects.all()
    }
    abcd = Request_To_Chat.objects.all()


  # for names in abcd:
   #     if names.requestor == request.POST['profile_name']  :
    #         return render(request,'meet/req_to_chat.html',chat)
            
    
    if request.method == 'POST' :
                s = request.POST['profile_name']
                accept = Profile.objects.get(name = s)
                user = User.objects.get(username=request.user.username)
                req = Profile.objects.get(name = user )
                for name in abcd:
                    if name.requestor == req and name.acceptor == accept:
                        return render(request,'meet/req_to_chat.html',chat)
                    elif name.requestor == accept and name.acceptor == req:
                        return render(request,'meet/req_to_chat.html',chat)





                data = Request_To_Chat(requestor =req, acceptor = accept)
                data.save()
    
    return render(request,'meet/req_to_chat.html',chat)
    
def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name = room)

    return render(request,'meet/room.html',{
        'username' : username,
        'room': room,
        'room_details': room_details
    })

def chat(request):

    rooms = {
        'name': Room.objects.all()
    }
   

    return render (request,'meet/chats.html', rooms )
def check(request):
    user1 = request.user.username
    room = request.POST['room_name']
    msg = Message.objects.all() 
    ab =  Room.objects.filter(name = room).values()
    c = ab[0]
    room_no = str(c['id'])
   

    for msg_instance in msg:
        if msg_instance.room==room_no:
            if msg_instance.user != user1:
                msg_instance.is_read = True
                msg_instance.save()
           
               



   
    return redirect('chat/'+ room + '?username='+ user1)

def send(request):
    message = request.POST['message']
    username =  request.POST['username']
    room_id = request.POST['room_id']
    new_message= Message.objects.create(value = message, user = username , room = room_id  )
    new_message.save()
    return HttpResponse('MEssage Sent Succesfully')

def ShowMessages(request,room):
    room_details = Room.objects.get(name = room)
    messages = Message.objects.filter(room = room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def UnreadMessages(request,room):
    user1 = request.user.username
    room_details = Room.objects.get(name = room)
    messages = Message.objects.filter(room = room_details.id)
    count = 0
    for a in messages:
        if a.user != user1:
            if a.is_read == False:
                count+=1
    op = {'count1':count}
     
    
    return HttpResponse(count)


def search(request):
    query = request.GET['query']
    profiles = Profile.objects.filter(name__icontains=query)

    return render(request,'meet/search.html',{'profiles':profiles})