from django import forms
from .models import Plato, PrevisionDiaria

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'precio']

class PrevisionForm(forms.ModelForm):
    class Meta:
        model = PrevisionDiaria
        fields = ['plato', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }