from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createpost/', include('api.createPost.urls')),
    path('signup/', include('api.signup.urls')),
    path('login/', include('api.login.urls')),
    path('my_profile/', include('api.profile.urls')),
    path('charities/',include('api.charities.urls')),
    path('follow/',include('api.follow.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
