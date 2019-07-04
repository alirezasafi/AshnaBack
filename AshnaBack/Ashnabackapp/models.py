from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User_model = get_user_model()

kind = (
    ('government organization' , 'سازمان دولتی'),
    ('charity organization' , 'سازمان خیریه'),
    ('non governmental Organization' , 'سازمان مردم نهاد'),
    ('Private organization' , 'سازمان خصوصی'),
    ('Public organization' , 'سازمان عمومی'),
    ('government organization' , 'سازمان دولتی'),
    
)
fieldofactivity = (
    ('Healthcare','بهداشت و درمان'),
    ('Education','اموزش'),
    ('Ability and rehabilitation','توانایی و بازپروری'),
    ('Maintenance and care','نگهداری و سرپرستی'),
)

class Charity(models.Model):
    Charity_User = models.OneToOneField(User_model, on_delete=models.CASCADE, related_name='Charity', default=None)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='images/',blank=True,null=True)
    ManagingDirector = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    Email = models.EmailField(unique=True, max_length=100)
    Address = models.TextField(blank=True)
    CreationData = models.DateField(auto_now_add=True)
    Kind = models.CharField(choices=kind,max_length=100)
    FieldOFactivity = models.CharField(choices=fieldofactivity,max_length=100)
    Bio = models.TextField(blank=True)
    Password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name


class Person(models.Model):
    Person_User = models.OneToOneField(User_model, on_delete=models.CASCADE, related_name='Benefactor',
                                           default=None)
    Image = models.ImageField(upload_to='images/',blank=True,null=True)
    Name = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    TotalSupport = models.CharField(max_length=100, blank=True, null=True)
    Password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name


class Post(models.Model):
    Subject = models.CharField(max_length=100)
    Content = models.TextField(blank=True, null=True)
    Owner = models.ForeignKey(Charity, related_name='Post', on_delete=models.CASCADE)
    CreationData = models.DateField(auto_now_add=True)
    Image = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return self.Subject


class Relation(models.Model):
    Follower = models.ForeignKey(Person, related_name='follower', on_delete=models.CASCADE)
    Followed = models.ForeignKey(Charity, related_name='followed', on_delete=models.CASCADE)
