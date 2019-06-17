from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView
)
from django.urls import resolve
from rest_framework.views import APIView
from rest_framework.response import Response
from Ashnabackapp.models import (
    Charity,
    Post,
    Person,
    Relation,
)
from .serializers import (
    CharityProfileSerializer,
    PersonProfileSerializer,
    PostsSerilizer,
    PostSerializer,
    FollowersSerializers
)

    
class ProfileView(RetrieveAPIView):

    lookup_field = 'Name'
    lookup_url_kwarg = 'Name'
    def get_queryset(self):
        Charity_obj = Charity.objects.filter(Charity_User_id=self.request.user.id)
        if Charity_obj.exists():
            return Charity.objects.filter(Name=Charity_obj[0].Name)
        Person_obj = Person.objects.filter(Person_User_id=self.request.user.id)
        return Person.objects.filter(Name=Person_obj[0].Name)
    def get_serializer_class(self):
        Charity_obj = Charity.objects.filter(Charity_User_id=self.request.user.id)
        if Charity_obj.exists():
            return CharityProfileSerializer
        return PersonProfileSerializer
        
        
class PostsView(ListAPIView):
    def get_queryset(self):
        Charity_obj = Charity.objects.filter(Charity_User_id=self.request.user.id)
        if Charity_obj.exists():
            return Charity.objects.filter(Name=Charity_obj[0].Name)
     

    def get_serializer_class(self):
        Charity_obj = Charity.objects.filter(Charity_User_id=self.request.user.id)
        if Charity_obj.exists():
            return PostsSerilizer
