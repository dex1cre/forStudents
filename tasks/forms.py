from django import forms
from .models import *

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('name',)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('number', 'description', 'variables', 'ask', 'variant_id', )
