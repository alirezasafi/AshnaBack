from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField
)
from django.contrib.auth import get_user_model

User = get_user_model()


class loginSerializer(ModelSerializer):
    Email = EmailField(required=True)
    Password = CharField()
    
    class Meta():
        model = User
        fields = (
            'Email',
            'Password'
        )
