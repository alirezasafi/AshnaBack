# from rest_framework.generics import (
#     CreateAPIView,
# )
# from rest_framework import status
# from django.contrib.auth import (
#     authenticate,
#     login,
# )
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_200_OK
from rest_framework.response import Response
from .serializers import (
    CharitySighnupSerializer,
    PersonSignupSerializer
)
from rest_framework.permissions import AllowAny

from Ashnabackapp.models import Charity
from Ashnabackapp.models import Person
user_model = get_user_model()
class CharitySignup(APIView):
    serializer_class = CharitySighnupSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        # print(request.data)
        # data = data['data']
        name = data['Name']
        managingdirector = data['ManagingDirector']
        email = data['Email']
        phonenumber = data['PhoneNumber']
        password = data['Password']
        confirmpassword = data['ConfirmPassword']
        response = {'Error': "", "Email": "", "Password": ""}
        Charity_obj = Charity.objects.filter(Email=email)
        if password != confirmpassword:
            response['Error'] = "password isnt match"
        elif not email:
            response['Error'] = 'Email is required'
        elif Charity_obj.exists():
            response['Error'] = 'User signed up'
        else:
            user_obj = user_model.objects.create_user(username=name, password=password, email=email)
            user_obj.save()
            Charity_obj = Charity(
                Charity_User=user_obj,
                Name=name,
                ManagingDirector=managingdirector,
                PhoneNumber=phonenumber,
                Email=email,
                )
            Charity_obj.Password = password
            Charity_obj.save()
            response['Email'] = email
            response['Password'] = password
            # serializer = CharitySighnupSerializer(data=response)
            # response = serializer.initial_data
            print(response)
            return Response(response, status=HTTP_200_OK)
        # serializer = CharitySighnupSerializer(data=response)
        # response = serializer.initial_data
        
        return Response(response, status=HTTP_400_BAD_REQUEST)


class PersonSignup(APIView):
    serializer_class = PersonSignupSerializer
    # queryset = Person.objects.all()
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        data = request.data
        name = data['Name']
        email = data['Email']
        phonenumber = data['PhoneNumber']
        password = data['Password']
        confirmpassword = data['ConfirmPassword']
        response = {'Error': "", "Email": "", "Password": ""}
        Person_obj = Person.objects.filter(Email=email)
        if password != confirmpassword:
            response['Error'] = "password isnt match"
        elif not email:
            response['Error'] = 'Email is required'
        elif Person_obj.exists():
            response['Error'] = 'User signed up'
        else:
            user_obj = user_model.objects.create_user(username=name, password=password, email=email)
            user_obj.save()
            Person_obj = Person(
                Person_User=user_obj,
                Name=name,
                PhoneNumber=phonenumber,
                Email=email,
            )
            Person_obj.Password = password
            Person_obj.save()
            response['Email'] = email
            response['Password'] = password
            serializer = CharitySighnupSerializer(data=response)
            response = serializer.initial_data
            return Response(response, status=HTTP_200_OK)
        serializer = CharitySighnupSerializer(data=response)
        response = serializer.initial_data
        return Response(response, status=HTTP_400_BAD_REQUEST)
    #