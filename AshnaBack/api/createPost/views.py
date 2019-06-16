from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from rest_framework.response import Response
from .serializers import CharityPostSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from Ashnabackapp.models import Charity,Post

user_model=get_user_model()

class CharityPostRepots(APIView):
    serializer_class=CharityPostSerializer
    permissiona_class=[AllowAny]

    def post(self,request,*args,**kwargs):
        data=request.data
        response={'Error':'','Subject':'','Content':''}
        subject=data['Subject']
        content=data['Content']
        charity_id=data['Owner']
        owner_obj=Charity.objects.filter(id=charity_id)

        if not subject:
            response['Error']='subject does not entered'
        elif not content:
            response['Error']='content does not entered'
        elif not owner_obj.exists():
            response['Error']='owner does not selected'
        else:
            # import pprint
            # pprint.pprint(request.data)
            new_post=Post(
                Subject=subject,
                Content=content,
                Owner=owner_obj[0]
            )
            new_post.save()
            response['Subject']=subject
            response['Content']=content
            

            return Response(response,HTTP_201_CREATED)
            # print(request.data)
            # return Response(response,HTTP_200_OK)
        return Response(response,HTTP_400_BAD_REQUEST)