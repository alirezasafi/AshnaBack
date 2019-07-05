from django.urls import path
from .views import ProfileUpdataeApiview


app_name = 'settings'
urlpatterns = [
    path('<Name>',ProfileUpdataeApiview.as_view(),name='profname')
]
