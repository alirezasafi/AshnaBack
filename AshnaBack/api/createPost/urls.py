from django.urls import include,path

from .views import CharityPostRepots

urlpatterns = [
    path('',CharityPostRepots.as_view(),name='charityPostReport'),
    
]
