from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass #for now, we can leave it empty, but we can add custom fields later if needed.

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', through='FollowRelation', symmetrical=False, related_name='following') # if a user is following another user, the other user is not necessarily following them back. The related_name 'following' allows us to access the users that a given user is following.

    def __str__(self):
        return f"{self.user.username} {self.pk}"

class FollowRelation(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followed_by') #if followers profile is deleted, relationship is also deleted
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follows') #if following profile is deleted, relationship is also deleted
    created = models.DateTimeField(auto_now_add=True) #when the relationship was created

    class Meta:
        unique_together = ('follower', 'following') #ensures that a user cannot follow the same user multiple times

    def __str__(self):
        return f"{self.follower.user.username} follows {self.following.user.username}"