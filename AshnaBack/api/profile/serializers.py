from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from Ashnabackapp.models import Charity,Post,Person,Relation



class PostSerializer(ModelSerializer):
    Image = SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'Image',
            'Subject',
            'Content',
            'CreationData'
        )
    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image
    
    
class FollowersSerializers(ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'Name',
        )

class FollowingsSerializers(ModelSerializer):
    class Meta:
        model = Charity
        fields = (
            'Name',
        )

class CharityProfileSerializer(ModelSerializer):
    Followers = SerializerMethodField()
    Image = SerializerMethodField()
    class Meta:
        model = Charity
        fields = (
            'Name',
            'ManagingDirector',
            'Image',
            'PhoneNumber',
            'PhoneNumber',
            'Email',
            'Address',
            'CreationData',
            'Kind',
            'FieldOFactivity',
            'Bio',
            'Followers',
        )
    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image
    def get_Followers(self,instance):
        relations = Relation.objects.filter(Followed_id = instance.id)
        Followers = []
        for rel in relations:
            Followers.append(rel.Follower)
        Followers = FollowersSerializers(Followers,many=True).data
        return Followers
        

class PersonProfileSerializer(ModelSerializer):
    Followings = SerializerMethodField()
    Image = SerializerMethodField()
    class Meta:
        model = Person
        fields = (
            'Name',
            'Image',
            'PhoneNumber',
            'Email',
            'TotalSupport',
            'Password',
            'Followings',
        )
    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image
    
    def get_Followings(self,instance):
        relations = Relation.objects.filter(Follower_id=instance.id)
        Followings = []
        for rel in relations:
            Followings.append(rel.Followed)
        Followings = FollowingsSerializers(Followings, many=True).data
        return Followings
    
    
class PostsSerilizer(ModelSerializer):
    Image = SerializerMethodField()
    Posts = SerializerMethodField()
    class Meta:
        model = Charity
        fields = (
            'Name',
            'Image',
            'Posts',
            
        )
    def get_Image(self, instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image

    def get_Posts(self, instance):
        Posts = Post.objects.filter(Owner_id=instance.id)
        Posts = PostSerializer(Posts, many=True).data
        return Posts