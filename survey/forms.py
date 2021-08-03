from django.forms import ModelForm
from .models import SurveyUser
from django import  forms
class SigninForm(ModelForm):
    class Meta:
        model = SurveyUser
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.TextInput(attrs={'class': 'input'}),
            'phone': forms.TextInput(attrs={'class': 'input'}),
        }