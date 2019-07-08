from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from Ashnabackapp.models import (
    Charity,
    Person,
    Relation,
)
from django.db.models import CharField

class PersonSerializers(ModelSerializer):
    Image = SerializerMethodField()
    class Meta:
        model = Person
        fields = (
            'id',
            'Name',
            'Image',
        )
    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image
        
class FollowersSerializers(ModelSerializer):
    Followers = SerializerMethodField()
    class Meta:
        model = Charity
        fields = (
            'Name',
            'Followers'
        )
    def get_Followers(self, instance):
        relations = Relation.objects.filter(Followed_id = instance.id)
        Followers = []
        for rel in relations:
            Followers.append(rel.Follower)
        Followers = PersonSerializers(Followers,many=True).data
        return Followers

class CharitySerializers(ModelSerializer):
    Image = SerializerMethodField()
    class Meta:
        model = Charity
        fields = (
            'id',
            'Name',
            'Image',
        )
    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image
    
class FollowingsSerializers(ModelSerializer):
    Followings = SerializerMethodField()
    class Meta:
        model = Person
        fields = (
            'Name',
            'Followings'
        )
    def get_Followings(self,instance):
        relations = Relation.objects.filter(Follower_id = instance.id)
        Followings = []
        for rel in relations:
            Followings.append((rel.Follower))
        Followings = CharitySerializers(Followings,many=True).data
        return Followings

class PersonFollowCharotySerializer(ModelSerializer):
    Follower=CharField()
    Followed=CharField()
    class Meta:
        model=Relation
        fields=('id','Follower','Followed')
        
        