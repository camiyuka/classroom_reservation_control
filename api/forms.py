from django import forms
from .repository import ClassroomRepository
from datetime import datetime

class ClassroomForm(forms.Form):
    name = forms.CharField(required=False)
    capacity = forms.CharField()
    number = forms.IntegerField(required=False)
    location = forms.CharField(required=False)

class ClassroomReservationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ClassroomReservationForm, self).__init__(*args, **kwargs)

        client = MongoClient('mongodb://localhost:27017/')
        db = client['classroom_reservation_ACL']
        collection = db['classrooms']  
        
        classrooms = [(str(classroom['_id']), classroom['name']) for classroom in collection.find()]
        
        self.fields['classroom'] = forms.ChoiceField(choices=classrooms)
        
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        
        # Validar se o tempo de início é anterior ao tempo final
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("A hora de início deve ser antes da hora final.")
        
        return cleaned_data

