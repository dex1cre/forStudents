from django import forms
from .models import *

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('name',)
