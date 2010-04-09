#/apps/glossaries/
from django.db import models

class Glossary(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField('languages.Language')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "glossaries"
    
class GlossaryTerm(models.Model):
    term_id = models.IntegerField()
    language = models.ForeignKey('languages.Language')
    term = models.CharField(max_length=100)
    definition = models.TextField()
    glossary = models.ForeignKey(Glossary)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def get_languages(self):
        return ', '. join(str(x) for x in self.glossary.languages.all())  
        
    def __unicode__(self):
        return self.term
        
    class Meta:
        ordering = ["term"]
        verbose_name_plural = "glossary terms"
        unique_together = (("term_id", "language", "glossary"),)
