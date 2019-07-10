from rest_framework.generics import (
    RetrieveUpdateAPIView
)
from rest_framework.response import Response
from .serializers import (
    CharitySettingSerializer,
    PersonSettingSerializer
)
from Ashnabackapp.models import (
    Charity,
    Person,
)
from django.contrib.auth import get_user_model
User_model = get_user_model()


class ProfileUpdataeApiview(RetrieveUpdateAPIView):
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
            return CharitySettingSerializer
        return PersonSettingSerializer
    def put(self, request, *args, **kwargs):
        data = request.data
        user = User_model.objects.filter(id=request.user.id)[0]
        Charity_obj = Charity.objects.filter(Charity_User_id=request.user.id)
        if Charity_obj.exists():
            charity = Charity_obj[0]
            user.email = data['Email']
            user.username = data['Name']
            Charity.Name = data['Name']
            if data['Image'] != "null":
                charity.Image = data['Image']
            charity.ManagingDirector = data['ManagingDirector']
            charity.PhoneNumber = data['PhoneNumber']
            charity.Email = data['Email']
            charity.Address = data['Address']
            charity.Bio = data['Bio']
            user.save()
            charity.save()
            response = {"Error": ""}
            return Response(response)
        else:
            
            Person_obj = Person.objects.filter(Person_User_id=request.user.id)[0]
            user.email = data['Email']
            user.username = data['Name']
            Person_obj.Name = data['Name']
            if data['Image'] != "null":
                Person_obj.Image = data['Image']
            Person_obj.PhoneNumber = data['PhoneNumber']
            Person_obj.Email = data['Email']
            user.save()
            Person_obj.save()
            response = {"Error":""}
            return Response(response)
        
