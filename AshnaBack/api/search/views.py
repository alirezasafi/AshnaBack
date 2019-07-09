from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from Ashnabackapp.models import (Person,Charity,Relation)
from .serializers import (
    CharitiesSerialzer,
    CharityDetailSerializer,
    CharityPostSerializer,
    CharityFollowersSerializer
)

from rest_framework.permissions import AllowAny


class CharitiesListApiView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CharitiesSerialzer
    queryset = Charity.objects.all()
    
    def post(self, request, *args, **kwargs):
        data = request.data
        name = data['searchBar']
        
        fieldofactivity = data['FieldOFactivity']
        if name:
            Charities = Charity.objects.filter(Name=name)
            response = [CharitiesSerialzer(instance=Charities[0]).data]
            return Response(response)
        else:
            Charities = Charity.objects.filter(FieldOFactivity=fieldofactivity)
            response = []
            for charity in Charities:
                response.append(CharitiesSerialzer(instance=charity).data)
            return Response(response)
            


class ChairtyDetailApiView(RetrieveAPIView):
    permission_classes = [AllowAny]
    lookup_field = 'Name'
    lookup_url_kwarg = 'NameOfCharity'
    def get(self, request,*args, **kwargs):
        print(self.request.parser_context['kwargs']['NameOfCharity'])
        charity_name = request.parser_context['kwargs']['NameOfCharity']
        user_id = request.user.id
        response = {}
        Charity_obj = Charity.objects.filter(Name=charity_name)[0]
        if request.user:
            person_obj = Person.objects.filter(Person_User_id=user_id)[0]
            relation = Relation.objects.filter(Follower_id=person_obj.id,Followed_id=Charity_obj.id)

            if len(relation)!=0:
                response = CharityDetailSerializer(Charity_obj).data
                response['IsFollowed'] = True
            else:
                response = CharityDetailSerializer(Charity_obj).data
                response['IsFollowed'] = False
            return Response(response)
        response = CharityDetailSerializer(Charity_obj).data
        response['IsFollowed'] = False
        return Response(response)

class CharityPostsView(RetrieveAPIView):
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'NameOfCharity'
    lookup_field = 'Name'
    def get(self, request, *args, **kwargs):
        print(self.request.parser_context['kwargs']['NameOfCharity'])
        charity_name = request.parser_context['kwargs']['NameOfCharity']
        user_id = request.user.id
        response = {}
        Charity_obj = Charity.objects.filter(Name=charity_name)[0]
        if request.user:
            person_obj = Person.objects.filter(Person_User_id=user_id)[0]
            relation = Relation.objects.filter(Follower_id=person_obj.id, Followed_id=Charity_obj.id)
        
            if len(relation) != 0:
                response = CharityPostSerializer(Charity_obj).data
                response['IsFollowed'] = True
            else:
                response = CharityPostSerializer(Charity_obj).data
                response['IsFollowed'] = False
            return Response(response)
        response = CharityPostSerializer(Charity_obj).data
        response['IsFollowed'] = False
        return Response(response)
    
    
class CharityFollowersView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CharityFollowersSerializer
    lookup_url_kwarg = 'NameOfCharity'
    lookup_field = 'Name'
    queryset = Charity.objects.filter()
