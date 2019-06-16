from rest_framework.serializers import ModelSerializer,CharField
from Ashnabackapp.models import Post



class CharityPostSerializer(ModelSerializer):
    Subject =CharField(required=True)
    Content =CharField()
    class Meta:
        model=Post
        fields=('Subject','Content','Image')