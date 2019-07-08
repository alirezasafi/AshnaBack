from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from Ashnabackapp.models import (
    Charity,
    Person,
    Relation,
)


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