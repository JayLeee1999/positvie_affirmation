from django.db import models

# Create your models here.
class Article(models.Model):
    nickname = models.CharField(max_length=50)
    emotion = models.CharField(max_length=50)
    affirmation = models.TextField()
    cdate = models.DateField(auto_now_add = True)
