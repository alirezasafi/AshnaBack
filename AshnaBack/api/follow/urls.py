from django.urls import path, include
from .views import FollowersView

urlpatterns = [
    path('followers/',FollowersView.as_view(),name='get_Followers'),
]