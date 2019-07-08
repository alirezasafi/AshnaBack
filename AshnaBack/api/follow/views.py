from rest_framework.generics import (
    ListAPIView
)
from Ashnabackapp.models import (
    Charity,
    Person,
)
from .serializers import (
    FollowersSerializers,
    FollowingsSerializers
)
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