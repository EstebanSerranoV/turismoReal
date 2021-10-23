from django.db.models import fields
from rest_framework.fields import ReadOnlyField
from .models import Departamento
from rest_framework import serializers



class DepartamentoSerializer(serializers.ModelSerializer):
    nombre_departamento = serializers.CharField(read_only=True, source="nombre")

    class Meta:
        model = Departamento
        fields = '__all__'

    def validate_nombre(self, value):
        existe = Departamento.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este Departamento ya existe")
        return value