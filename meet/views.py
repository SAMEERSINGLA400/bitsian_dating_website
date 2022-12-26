from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Profile,Request_To_Chat
from .models import Request_To_Chat,Block
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView , UpdateView
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
    fields =['name','likes']

    def form_valid(self,form):
        form.instance.username = self.request.user 
        return super().form_valid(form)

class ProfileUpdateView( LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Profile
    fields =['name','likes']

    def form_valid(self,form):
        form.instance.username = self.request.user 
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
    
   