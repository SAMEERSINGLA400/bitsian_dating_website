from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'meet-home'), # meet-home used in template particularly css file
    path('about/',views.about,name = 'meet-about'),
    path('req_to_chat',views.req_to_chat,name ='meet-chat'),
]