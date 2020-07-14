from django.forms import ModelForm
from admin.models import AdminTable,ScheduleclassesTable
from django import forms
import re
import calendar


class  adminform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(adminform, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['contact_no'].widget.attrs['class'] = 'form-control'

    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=AdminTable
        fields='__all__'

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Password is mininum 8 digits')
        else:
            return password


class scheduleclass(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(scheduleclass, self).__init__(*args, **kwargs)
        self.fields['course'].widget.attrs['class'] = 'form-control'
        self.fields['duration'].widget.attrs['class'] = 'form-control'

    class Meta:
        model=ScheduleclassesTable
        fields='__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'time':forms.TimeInput(attrs={'type':'time','class':'form-control'})

        }