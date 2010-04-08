#/apps/languages/
from django.db import models
from django.contrib import admin

class Language(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ["id"]