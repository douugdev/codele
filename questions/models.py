from django.db import models

class Question(models.Model):
    languages = [
    ('NONE','Nenhuma'),
    ('JS','JavaScript'),
    ('PY', 'Python'),
    ('GML', 'Game Maker Language'),
    ('JV','Java'),
    ]
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    question = models.TextField()
    language = models.CharField(max_length=4, choices=languages, default='NONE')

    def __str__(self):
        return f'{self.title}'

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'An answer to {self.question.title}'
