from django.db import models as mo

# Create your models here.

class Topic(mo.Model):
    topic_name = mo.CharField(max_length=50,primary_key=True)
    
    def __str__(self):
        return self.topic_name

class Webpage(mo.Model):
    topic_name = mo.ForeignKey(Topic, on_delete=mo.CASCADE)
    name = mo.CharField(max_length=50, primary_key=True)
    url = mo.URLField()
    
    def __str__(self):
        return self.name

class AccessRecord(mo.Model):
    name = mo.ForeignKey(Webpage, on_delete=mo.CASCADE)    
    date = mo.DateField()
    author = mo.CharField(max_length=50)
    
    def __str__(self):
        return self.author
    