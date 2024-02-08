from django import forms
from app.models import *

#creating forms here

class IndiaForm(forms.ModelForm):
    class Meta:
        model = India
        fields = '__all__'

    