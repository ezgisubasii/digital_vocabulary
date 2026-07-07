from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from profiles.models import Profile

User = get_user_model()

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs): # this function is called when a new user is created. It creates a profile for the new user.
    if created:
        Profile.objects.create(user=instance)