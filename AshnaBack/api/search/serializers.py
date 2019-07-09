from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from ..follow.serializers import PersonSerializers
from ..profile.serializers import PostSerializer,FollowersSerializers
from Ashnabackapp.models import (
    Charity,
    Post,
    Relation,
)


class CharitiesSerialzer(ModelSerializer):
    FieldOFactivity = SerializerMethodField()
    url = SerializerMethodField()
    Image = SerializerMethodField()
    class Meta:
        model = Charity
        fields = (
            'url',
            'Name',
            'Image',
            'FieldOFactivity',
        )
    def get_FieldOFactivity(self,instance):
        return  instance.get_FieldOFactivity_display()
    def get_url(self,instance):
        return  "http://127.0.0.1:8000/charities/"+instance.Name
    def get_Image(self, instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image

class CharityDetailSerializer(ModelSerializer):
    Image = SerializerMethodField()
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

    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image



class CharityPostSerializer(ModelSerializer):
    Posts = SerializerMethodField()
    class Meta:
        model = Charity
        fields = (
            'id',
            'Name',
            'Image',
            'Posts',
        )
    def get_Posts(self,instance):
        Posts = Post.objects.filter(Owner_id=instance.id)
        Posts = PostSerializer(Posts,many=True).data
        return Posts
    
    
class CharityFollowersSerializer(ModelSerializer):
    Followers = SerializerMethodField()
    class Meta:
        model = Charity
        fields = (
            'id',
            'Name',
            'Image',
            'Followers',
        )
    def get_Followers(self,instance):
        relations = Relation.objects.filter(Followed_id=instance.id)
        Followers = []
        for rel in relations:
            Followers.append(rel.Follower)
        Followers = PersonSerializers(Followers, many=True).data
        return Followers