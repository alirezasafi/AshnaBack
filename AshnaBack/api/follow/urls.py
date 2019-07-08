from django.urls import path, include
from .views import (
    FollowersView,
    FollowingsView,
)

urlpatterns = [
    path('followers/',FollowersView.as_view(),name='get_Followers'),
    path('followings/',FollowingsView.as_view(),name='get_Followings')
]