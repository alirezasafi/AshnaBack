from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField
)
from django.contrib.auth import get_user_model

User = get_user_model()


<<<<<<< HEAD
=======

User = get_user_model()
>>>>>>> 193fd795067ac808857940aab346d77625a72dce
class loginSerializer(ModelSerializer):
    Email = EmailField(required=True)
    Password = CharField()
    
    class Meta():
        model = User
        fields = (
            'Email',
            'Password'
        )
<<<<<<< HEAD
=======
        
>>>>>>> 193fd795067ac808857940aab346d77625a72dce
