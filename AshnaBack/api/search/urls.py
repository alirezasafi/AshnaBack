from django.urls import  path,include
from .views import (
    CharitiesListApiView,
    ChairtyDetailApiView,
    CharityPostsView,
    CharityFollowersView
)
app_name = 'prof'
urlpatterns = [
    path('',CharitiesListApiView.as_view(),name = 'Chariteis'),
    path('<NameOfCharity>/', ChairtyDetailApiView.as_view(), name='CharityProf'),
    path('<NameOfCharity>/posts',CharityPostsView.as_view(),name='CahrityPosts'),
    path('<NameOfCharity>/followers',CharityFollowersView.as_view(),name='CharityFollowers'),
]

