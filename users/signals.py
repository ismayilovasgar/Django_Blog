from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile


# To create the profile picture
@receiver(post_save, sender=User, dispatch_uid="my_unique_identifier")
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# To save the profile picture
@receiver(post_save, sender=User, dispatch_uid="my_unique_identifier")
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
