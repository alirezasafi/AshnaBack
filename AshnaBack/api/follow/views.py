from rest_framework.generics import (
    ListAPIView,
    
)
from Ashnabackapp.models import (
    Charity,
    Person,
    Relation
)
from .serializers import (
    FollowersSerializers,
    FollowingsSerializers,
    PersonFollowCharotySerializer,

)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class FollowersView(ListAPIView):
    def get_queryset(self):
        Charity_obj = Charity.objects.filter(Charity_User_id=self.request.user.id)
        if Charity_obj.exists():
            return Charity.objects.filter(Name=Charity_obj[0].Name)

    def get_serializer_class(self):
        Charity_obj = Charity.objects.filter(Charity_User_id=self.request.user.id)
        if Charity_obj.exists():
            return FollowersSerializers
        
        
class FollowingsView(ListAPIView):
    def get_queryset(self):
        Person_obj = Person.objects.filter(Person_User_id=self.request.user.id)
        if Person_obj.exists():
            return Person.objects.filter(Name=Person_obj[0].Name)
        
    def get_serializer_class(self):
        Person_obj = Person.objects.filter(Person_User_id=self.request.user.id)
        if Person_obj.exists():
            return FollowingsSerializers
user_model=get_user_model()
class PersonFollowCharity(APIView):
    serializer_class=PersonFollowCharotySerializer
    permission_class=[AllowAny]
    def post(self,request,*args,**kwargs):
        data=request.data
        # print(data)
        # print(request.data['Follower'])
        response={'Error':''}
        person_id=data['Follower']
        charity_id=data['Followed']
        person_obj=Person.objects.filter(id=person_id)[0]
        charity_obj=Charity.objects.filter(id=charity_id)[0]
        if not person_obj:
            response['Error']='Person Does Not Enterd.'
        elif not charity_obj:
            response['Error']='Charity Does Not Enterd.'
        else:
            follow=Relation(
                Follower=person_obj,
                Followed=charity_obj
            )
            if follow not in Relation.objects.all():
                follow.save()
                return Response(response,HTTP_200_OK)
            else:
                # TODO:fix bug in following
                response['Error']='Relation has been added.'
                
            
               
        return Response(response,HTTP_400_BAD_REQUEST)
