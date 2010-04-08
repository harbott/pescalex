#/apps/news/
from django.db import models
from django.contrib import admin

class News(models.Model):
    headline = models.CharField(max_length=100)
    author = models.ForeignKey('users.UserProfile', limit_choices_to={'groups__in': [1]})
    date = models.DateTimeField()
    article = models.TextField()
    published = models.BooleanField()
    
    def __unicode__(self):
        return self.headline
        
    class Meta:
        ordering = ["published"]
        verbose_name_plural = "news"