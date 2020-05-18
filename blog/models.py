from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    post = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(default='blog_pics/monument.jpg', upload_to='blog_pics')

    def __str__(self):
        return f'{self.title}'
