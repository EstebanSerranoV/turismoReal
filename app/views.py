from django.shortcuts import render, redirect, get_object_or_404
from .models import Departamento, Reserva
from .forms import DepartamentoForm, CustomUserCreationForm, ReservaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import serializers, viewsets
from .serializers import DepartamentoSerializer
# Create your views here.

#Api
class DepartamentoViewset(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer



def home(request):
    departamentos = Departamento.objects.all()
    data = {
        'departamentos': departamentos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    return render(request, 'app/galeria.html')

@permission_required('app.add_departamento')
def agregar_deptos(request):

    data = {
        'form': DepartamentoForm()
    }

    if request.method == 'POST':
        formulario = DepartamentoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data["form"] = formulario


    return render(request, 'deptos/agregar.html', data)


@permission_required('app.view_departamento')
def listarDeptos(request):
    departamentos = Departamento.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(departamentos, 5)
        departamentos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': departamentos,
        'paginator': paginator
    }
    return render(request, 'deptos/listar.html', data)

@permission_required('app.change_departamento')
def modificarDeptos(request, id_depa):

    departamentos = get_object_or_404(Departamento, id_depa=id_depa)

    data = {
        'form': DepartamentoForm(instance=departamentos)
    }

    if request.method == 'POST':
        formulario = DepartamentoForm(data=request.POST, instance=departamentos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarDep")
        data["form"] = formulario

    return render(request, 'deptos/modificar.html', data)

@permission_required('app.delete_departamento')
def eliminarDptos(request, id_depa):
    departamentos = get_object_or_404(Departamento, id_depa=id_depa)
    departamentos.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarDep")


def registro(request): 
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #Redirigir al HOME
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)



    #LOGIN_REQUIRED PARA RESERVA
def reserva(request):
    data = {
        'form': ReservaForm()
    }

    if request.method == "POST":
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Esta lista tu Reserva")
        else:
            data["form"] = formulario

    return render(request, 'app/reserva.html', data)