from django.forms import EmailInput, ModelForm, TextInput

from personas.models import Domicilio, Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle': TextInput(attrs={'type': 'number'})
        }