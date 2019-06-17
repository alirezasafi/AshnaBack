from rest_framework.views import APIView
from .serializers import CharityloginSerializer,PersonloginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_200_OK
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate,
    logout,
    login
)
from Ashnabackapp.models import Charity
from Ashnabackapp.models import Person

user_model = get_user_model()
class CharityLogin(APIView):
    serializer_class = CharityloginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        email = data['Email']
        password = data['Password']
        response = {'Error': "", "Email": "", "Password": ""}
        Charity_obj = Charity.objects.filter(Email=email)
        print(Charity_obj)
        if not email:
            response['Error'] = 'Email is required'
        elif not Charity_obj.exists():
            response['Error'] = 'User not found'
        elif Charity_obj[0].Password != password:
            response['Error'] = 'Password is incorect'
        else:
            name = Charity_obj[0].Name
            user = authenticate(request, username=name, password=password)
            login(request, user)
            response['Email'] = email
            response['Password'] = password
            # serializer = CharityloginSerializer(data=response)
            # response = serializer.initial_data
            return Response(response, status=HTTP_200_OK)
        # serializer = CharityloginSerializer(data=response)
        # response = serializer.initial_data
        return Response(response, status=HTTP_400_BAD_REQUEST)
    
    
class PersonLogin(APIView):
    serializer_class = PersonloginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request,*args,**kwargs):
        data = request.data
        email = data['Email']
        password = data['Password']
        response = {'Error': "", "Email": "", "Password": ""}
        Person_obj = Person.objects.filter(Email=email)
        if not email:
            response['Error'] = 'Email is required'
        elif not Person_obj.exists():
            response['Error'] = 'User not found'
        elif Person_obj[0].Password != password:
            response['Error'] = 'Password is incorect'
        else:
            name = Person_obj[0].Name
            user = authenticate(request, username=name, password=password)
            login(request, user)
            response['Email'] = email
            response['Password'] = password
            # serializer = CharityloginSerializer(data=response)
            # response = serializer.initial_data
            return Response(response, status=HTTP_200_OK)
        # serializer = PersonloginSerializer(data=response)
        # response = serializer.initial_data
        return Response(response, status=HTTP_400_BAD_REQUEST)