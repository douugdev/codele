from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    post = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
