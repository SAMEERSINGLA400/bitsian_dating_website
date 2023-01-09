from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView, ProfileCreateView, ProfileUpdateView,BlockView
from users.views import ReportView 

urlpatterns = [
    path('',ProfileListView.as_view(),name = 'meet-home'),
    path('profile/new/',ProfileCreateView.as_view(),name = 'profile-create'),
    path('profile/<int:pk>',ProfileDetailView.as_view(),name = 'profile-detail'),
    path('<int:pk>/accepted',views.accepted,name = 'accepted'),
    path('profile/<int:pk>/update/',ProfileUpdateView.as_view(),name = 'profile-update'),  # meet-home used in template particularly css file
    path('about/',views.about,name = 'meet-about'),
    path('req_to_chat',views.req_to_chat,name ='meet-chat'),
    path('profile/block_user',views.block_user,name ='meet-block'),
    path('profile/new/',ProfileCreateView.as_view(),name = 'profile-create'),
    path('report/',ReportView.as_view(),name = 'profile-report'),
    path('str<room>/',views.room,name= 'room'),
    path('chat/',views.chat,name= 'chat'),
    path('<str:room>/',views.room,name = 'room'),

    path('block/',BlockView.as_view(),name = 'profile-block')

]