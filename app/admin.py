from django.contrib import admin
from .models import  Administrador, Cargo, CheckIn, CheckOut, Cliente, Comuna, Conductor, Departamento, Direccion, Edificio,\
     Funcionario, InformeGanancia, InformeReserva, Inventario, Mantenimeinto, Provincia, Region, Reserva, Rol, ServicioExtra,\
          ServicioTransporte, Tour, Usuario, Vehiculo, Acompaniante, Contacto
from .forms import DepartamentoForm

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    form = DepartamentoForm




admin.site.register(Administrador)
admin.site.register(Cargo)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(Conductor)
admin.site.register(Departamento)
admin.site.register(Direccion)
admin.site.register(Edificio)
admin.site.register(Funcionario)
admin.site.register(InformeReserva)
admin.site.register(InformeGanancia)
admin.site.register(Inventario)
admin.site.register(Mantenimeinto)
admin.site.register(Provincia)
admin.site.register(Region)
admin.site.register(Reserva)
admin.site.register(Rol)
admin.site.register(ServicioExtra)
admin.site.register(ServicioTransporte)
admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(Acompaniante)
admin.site.register(Tour)
admin.site.register(Contacto)


