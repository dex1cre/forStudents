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

class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = ('name', 'subject_id',)
