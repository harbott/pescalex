#/apps/users/
from django.db import models
from django.contrib.auth.models import User

class UserProfile(User):
    company = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=30, blank=True)
        
    def __unicode__(self):
        return self.first_name +" "+ self.last_name