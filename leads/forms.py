from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_bootstrap5.bootstrap5 import BS5Accordion
from .models import Lead
User = get_user_model()
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = {
            'first_name',
            'last_name',
            'age',
            'agent'
        }

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

class CustomUserCreationForm(UserCreationForm):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Save'))
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

