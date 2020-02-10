from django import forms

from .models import Assignment


class Assignment_list(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('student_name','document_name','coursework_title','pdf')