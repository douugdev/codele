from rest_framework import serializers
from blog.models import Post
from questions.models import Question, Answer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'author', 'answer']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    answers = AnswerSerializer(many=True, read_only=True)


