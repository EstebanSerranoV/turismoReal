from django import forms
from django.forms import fields, widgets
from .models import Departamento, Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError







class DepartamentoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    tarifa = forms.IntegerField(min_value=1, max_value=1500000)


    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]      
        existe = Departamento.objects.filter(nombre__iexact=nombre).exists()  
    
        if existe:
           raise ValidationError("Este nombre ya existe")
        return nombre

    class Meta:
        model = Departamento
        fields = '__all__'

        widgets = {
            "fecha_fabvricacion":forms.SelectDateWidget()
        }
    




class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]



class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'

        widgets = {
            "fecha_inicio": forms.SelectDateWidget(),
            "fecha_fin": forms.SelectDateWidget()
        }
