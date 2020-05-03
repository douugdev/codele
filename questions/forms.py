from django.forms import ModelForm
from django.forms import ValidationError
from .models import Question

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['author', 'title', 'question', 'language']

    def clean_title(self):
        title = self.cleaned_data['title']
        title = title.capitalize()
        return title

    def clean_question(self):
        bad_words = ['shit', 'fuck', 'ass', 'bitch']
        words = self.cleaned_data['question'].split()
        for word in words:
            if word.lower() in bad_words:
                word = "*"*len(word)
        return " ".join(words)
