from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    '''This function is to let the user update his profile (email and username)'''
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
