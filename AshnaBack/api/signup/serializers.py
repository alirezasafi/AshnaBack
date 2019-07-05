from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
    IntegerField,
    EmailField
)
from django.contrib.auth import get_user_model
from Ashnabackapp.models import Charity
from Ashnabackapp.models import Person

User = get_user_model()


class CharitySighnupSerializer(ModelSerializer):
    Name = CharField()
    ManagerName = CharField()
    Email = EmailField()
    PhoneNumber = CharField()
    Password = CharField()
    ConfirmPassword = CharField(label='Confirm Password')
    Address = CharField()
    Kind = CharField()
    class Meta():
        model = Charity
        fields = (
            'Name',
            'ManagerName',
            'Email',
            'Address',
            'PhoneNumber',
            'Password',
            'ConfirmPassword',
            'Kind',
            # 'Image'
        )

class PersonSignupSerializer(ModelSerializer):
    Name = CharField()
    Email = EmailField()
    PhoneNumber = CharField()
    Password = CharField()
    ConfirmPassword = CharField(label='Confirm Password')
    
    class Meta():
        model = User
        fields = (
            'Name',
            'Email',
            'PhoneNumber',
            'Password',
            'ConfirmPassword',
        )
