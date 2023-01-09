from django.contrib import admin
from .models import Profile,Request_To_Chat,Room,Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(Request_To_Chat)
admin.site.register(Room)
admin.site.register(Message)
