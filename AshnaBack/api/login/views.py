from rest_framework.views import APIView
from .serializers import loginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate,
    login
)
from rest_framework.authtoken.models import Token
from Ashnabackapp.models import Charity
from Ashnabackapp.models import Person

user_model = get_user_model()
<<<<<<< HEAD


=======
>>>>>>> 193fd795067ac808857940aab346d77625a72dce
class Login(APIView):
    serializer_class = loginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        email = data['Email']
        password = data['Password']
<<<<<<< HEAD
        response = {'Error': "", 'Token': "", 'Name': ""}
=======
        response = {'Error': "",'Token':"",'Name':""}
>>>>>>> 193fd795067ac808857940aab346d77625a72dce
        Charity_obj = Charity.objects.filter(Email=email)
        if Charity_obj.exists() == True:
            Charity_obj = Charity_obj[0]
            if Charity_obj.Password != password:
                response['Error'] = "password is incorrect"
            else:
                name = Charity_obj.Name
                Userobj = user_model.objects.filter(email=email)[0]
                token = Token.objects.filter(user=Userobj)[0]
                # user = authenticate(request, username=name, password=password)
                # login(request, user)
                response['Name'] = name
                response['Token'] = token.key
<<<<<<< HEAD
            
            return Response(response)
        
=======
                
            return Response(response)
            
>>>>>>> 193fd795067ac808857940aab346d77625a72dce
        
        else:
            Person_obj = Person.objects.filter(Email=email)
            if Person_obj.exists() == True:
                Person_obj = Person_obj[0]
                if Person_obj.Password != password:
                    response['Error'] = "password is incorrect"
                else:
                    name = Person_obj.Name
                    Userobj = user_model.objects.filter(email=email)[0]
                    token = Token.objects.filter(user=Userobj)[0]
                    response['Name'] = name
                    response['Token'] = token.key
                return Response(response)
            else:
                response['Error'] = "User not found"
                return Response(response)
