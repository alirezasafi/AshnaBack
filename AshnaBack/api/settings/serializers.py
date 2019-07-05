from rest_framework.serializers import ModelSerializer
from Ashnabackapp.models import (
    Charity,
    Person,
)
from django.contrib.auth import get_user_model
User_model = get_user_model()
class CharitySettingSerializer(ModelSerializer):
    class Meta:
        model = Charity
        fields = (
            'Name',
            'Image',
            'ManagingDirector',
            'PhoneNumber',
            'Email',
            'Address',
            'Kind',
            'FieldOFactivity',
            'Bio',
        )
    
class PersonSettingSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'Name',
            'Image',
            'PhoneNumber',
            'Email',
        )
        