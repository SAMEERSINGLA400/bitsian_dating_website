from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView, ProfileCreateView, ProfileUpdateView

urlpatterns = [
    path('',ProfileListView.as_view(),name = 'meet-home'),
    path('profile/new/',ProfileCreateView.as_view(),name = 'profile-create'),
    path('profile/<int:pk>',ProfileDetailView.as_view(),name = 'profile-detail'),
    path('profile/<int:pk>/update/',ProfileUpdateView.as_view(),name = 'profile-update'),  # meet-home used in template particularly css file
    path('about/',views.about,name = 'meet-about'),
    path('req_to_chat',views.req_to_chat,name ='meet-chat'),
]