from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100, primary_key=True)
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField(max_length=20)

class Access_Record(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)


    
