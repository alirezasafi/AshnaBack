from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from Ashnabackapp.models import Charity,Post,Person,Relation



class PostSerializer(ModelSerializer):
    Owner = SerializerMethodField()
    Image = SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'id',
            'Image',
            'Subject',
            'Content',
            'CreationDate',
            'Owner',
        )
    def get_Owner(self, instance):
        Owner = Charity.objects.filter(id=instance.Owner_id)[0]
        return Owner.Name
    
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
    Image = SerializerMethodField()
    class Meta:
        model = Charity
        fields = (
            'Name',
            'ManagingDirector',
            'Image',
            'PhoneNumber',
            'Email',
            'Address',
            'CreationDate',
            'Kind',
            'FieldOFactivity',
            'Bio',
            # 'Followers',
        )
    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image

class PersonProfileSerializer(ModelSerializer):
    Image = SerializerMethodField()
    class Meta:
        model = Person
        fields = (
            'Name',
            'Image',
            'PhoneNumber',
            'Email',
            'TotalSupport',
        )
    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image
    
    
    
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
    
    
class TimeLineSerializers(ModelSerializer):
    Image = SerializerMethodField()
    Posts = SerializerMethodField()
    class Meta:
        model = Person
        fields = (
            'id',
            'Name',
            'Image',
            'Posts',
        )
        
    def get_Image(self,instance):
        if not instance.Image:
            return None
        Image = "http://127.0.0.1:8000" + instance.Image.url
        return Image

    def get_Posts(self,instance):
        relation = Relation.objects.filter(Follower_id=instance.id).values_list('Followed_id', flat=True)
        posts = reversed(Post.objects.filter(Owner_id__in=relation).order_by('CreationDate'))
        print(posts)
        posts = PostSerializer(posts,many=True).data
        return posts
        