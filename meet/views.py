from django.shortcuts import render
from .models import Profile

# Create your views here.
 
def home(request):
    context = {
        'profiles': Profile.objects.all()

    }
    return render(request, 'meet/home.html',context)

def about(request):
    return render(request, 'meet/about.html')