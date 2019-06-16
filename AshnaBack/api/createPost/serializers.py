from rest_framework.serializers import ModelSerializer
from Ashnabackapp.models import Post



class CharityPostSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=('Subject','Content','Owner')