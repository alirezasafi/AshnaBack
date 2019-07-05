from django.urls import path,include
from .views import ProfileView,PostsView

app_name = 'my_profile'
urlpatterns = [
    path('<Name>',ProfileView.as_view(),name='profname'),
    path('posts/',PostsView.as_view(),name='Posts'),
    path('edit/', include('api.settings.urls')),
]
