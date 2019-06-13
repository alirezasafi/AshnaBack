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
    ManagingDirector = CharField()
    Email = EmailField()
    PhoneNumber = CharField()
    Password = CharField()
    ConfirmPassword = CharField(label='Confirm Password')
    
    class Meta():
        model = User
        fields = (
            'Name',
            'ManagingDirector',
            'Email',
            'PhoneNumber',
            'Password',
            'ConfirmPassword',
        )
    
    # def create(self, data):
    #     confirmpass = data['ConfirmPassword']
    #     email = data['Email']
    #     name = data['Name']
    #     password = data['Password']
    #     if password != confirmpass:
    #         raise ValidationError('Passsword isnt match')
    #     charity = Charity.objects.filter(Email=email)
    #     if charity.exists():
    #         raise ValidationError('User has alredy signuped')
    #     user_obj = User.objects.create_user(username=name, password=password, email=email)
    #     user_obj.save()
    #     Charity_obj = Charity(
    #         Charity_User=user_obj,
    #         Name=name,
    #         Email=email,
    #     )
    #     Charity_obj.Password = password
    #     Charity_obj.save()
    #     return data


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
    
    # def create(self, data):
    #     email = data['Email']
    #     name = data['Name']
    #     password = data['Password']
    #     confirmpass = data['ConfirmPassword']
    #     if password != confirmpass:
    #         raise ValidationError('Password isnt match')
    #     benefactor = Person.objects.filter(Email=email)
    #     if benefactor.exists():
    #         raise ValidationError('User has alredy signuped')
    #     user_obj = User.objects.create_user(username=name, password=password, email=email)
    #     user_obj.save()
    #     benfactor_obj = Person(
    #         Benefactor_User=user_obj,
    #         Name=name,
    #         Email=email,
    #         Password=password
    #     )
    #     benfactor_obj.save()
    #     return data