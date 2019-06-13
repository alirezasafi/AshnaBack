from django.urls import path,include
from .views import (
    CharityLogin,
    PersonLogin
)


urlpatterns = [
    path('charity/' , CharityLogin.as_view(),name = 'CharityLogin'),
    path('person/' , PersonLogin.as_view(),name = 'PersonLogin')
]