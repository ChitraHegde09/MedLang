from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Symptom

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class SymptomForm(forms.Form):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
