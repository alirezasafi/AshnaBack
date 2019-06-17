from django.urls import path
from .views import ProfileView


app_name = 'my_profile'
urlpatterns = [
    path('<Name>',ProfileView.as_view(),name='profname')
]
