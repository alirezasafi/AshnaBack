from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from Ashnabackapp.models import Charity
from .serializers import (
    CharitiesSerialzer,
    CharityDetailSerializer
)
from rest_framework.permissions import AllowAny


class CharitiesListApiView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CharitiesSerialzer
    queryset = Charity.objects.all()
    
    def post(self, request, *args, **kwargs):
        data = request.data
        name = data['searchBar']
        # kind = data['Kind']
        fieldofactivity = data['FieldOfActivity']
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
    serializer_class = CharityDetailSerializer
    queryset = Charity.objects.filter()
    lookup_field = 'Name'
    lookup_url_kwarg = 'NameOfCharity'