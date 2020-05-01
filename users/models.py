from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BADGES = [('ESTUDANTE', 'Estudante'), ('PROFESSOR','Professor'), ('MODERADOR', 'Moderador'), ('ADMIN', 'Admin'), ('FUNDADOR', 'Fundador')]
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    lessons_completed = models.PositiveSmallIntegerField(default=0)
    courses_completed = models.PositiveSmallIntegerField(default=0)
    last_lesson = models.TextField(max_length=100)
    banned = models.BooleanField(default=False)
    badge = models.CharField(max_length=10,choices=BADGES, default='STUDENT')

    def __str__(self):
        return f'{self.user.username} profile'
