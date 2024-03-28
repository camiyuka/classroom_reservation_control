from django import forms

class ClassroomForm(forms.Form):
    name = forms.CharField(required=False)
    capacity = forms.CharField()
    number = forms.IntegerField(required=False)
    location = forms.CharField(required=False)
    available_periods = forms.ListField(required=False)
