from rest_framework.generics import (
    ListAPIView
)
from Ashnabackapp.models import (
    Charity,
)
from .serializers import FollowersSerializers

class FollowersView(ListAPIView):
    def get_queryset(self):
        Charity_obj = Charity.objects.filter(Charity_User_id=self.request.user.id)
        if Charity_obj.exists():
            return Charity.objects.filter(Name=Charity_obj[0].Name)

    # def get_serializer_class(self):
    #     Charity_obj = Charity.objects.filter(Charity_User_id=self.request.user.id)
    #     if Charity_obj.exists():
    #         return FollowersSerializers