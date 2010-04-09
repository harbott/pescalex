#/apps/courses/
from django.db import models

class CoursePage(models.Model):
    course = models.ForeignKey('courses.Course')
    
    def __unicode__(self):
        return str(self.course)

class CoursePageContent(models.Model):
    course_page = models.ForeignKey('courses.CoursePage')
    name = models.CharField(max_length=100)
    content = models.TextField()
    language = models.ForeignKey('languages.Language')
    
    def __unicode__(self):
        return self.name + '|' + str(self.language)
        
    def get_name(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField('languages.Language')    
    serialized_tree = models.TextField(editable="False")

    class Meta:
        ordering = ["name"]    

    def __unicode__(self):
        return self.name    

    def get_html_tree(self):
        stripped = self.serialized_tree.strip()
        if stripped != '':
            return stripped
        return '<ul></ul>'