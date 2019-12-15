from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True, blank=True)  
    location = models.CharField(max_length=200, null=True, blank=True) # char field 'x,y'   x and y coordinates of a shop (or geo coordinates) 
    
    class Meta: 
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username


class Item(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=200, null=True, blank=True)
    is_purchased = models.BooleanField(default=False)

    class Meta:
        db_table = 'item_table'

    def __str__(self):
        return self.item_name + ' ' + self.profile.user.username


class Shop(models.Model):
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    items_available = models.CharField(max_length=1000, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True) # char field 'x,y'   x and y coordinates of a shop (or geo coordinates)

    class Meta:
        db_table = 'shop_table'

    def __str__(self):
        return self.owner_name + ' ' + self.location


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)