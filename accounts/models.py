from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    '''This defines the user model, which has the username and his confirmed email'''
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

def __str__(self):
    return self.user


