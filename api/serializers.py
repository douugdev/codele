from rest_framework import serializers
from blog.models import Post
from questions.models import Question, Answer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    
class Question(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


