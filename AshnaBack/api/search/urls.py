from django.urls import  path,include
from .views import (
    CharitiesListApiView,
    ChairtyDetailApiView
)
app_name = 'prof'
urlpatterns = [
    path('',CharitiesListApiView.as_view(),name = 'Chariteis'),
    path('<NameOfCharity>/', ChairtyDetailApiView.as_view(), name='CharityProf')
]

