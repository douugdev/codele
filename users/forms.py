from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise ValidationError("E-mail já existente")
            
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return " ".join(word.capitalize() for word in first_name.split())

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return " ".join(word.capitalize() for word in last_name.split())

    def clean_password(self):
        original_password = self.cleaned_data.get('password')
        if len(original_password) < 8:
            raise ValidationError("Senha muito curta")
        elif len(original_password) > 50:
            raise ValidationError("Senha muito longa")
        else:
            return original_password

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise ValidationError("Nome de usuário já existente")
        else:
            return username

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
