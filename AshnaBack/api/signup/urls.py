from django.urls import path,include
from .views import (
    CharitySignup,
    PersonSignup
)


urlpatterns = [
    path('charity/' , CharitySignup.as_view(),name = 'CharitySignup'),
    path('person/' , PersonSignup.as_view(),name = 'PersonSignup')
]