from django.urls import path, include
from .views import home, contacto, galeria, agregar_deptos, listarDeptos, modificarDeptos, eliminarDptos,\
    registro, DepartamentoViewset, reserva
from rest_framework import routers


router = routers.DefaultRouter()
router.register('depa', DepartamentoViewset)


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregarDep/', agregar_deptos, name="agregarDep"),
    path('listarDep/', listarDeptos, name="listarDep"),
    path('modificarDep/<id_depa>/', modificarDeptos, name="modificarDep"),
    path('eliminarDep/<id_depa>/', eliminarDptos, name="eliminarDep"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
     path('reserva/', reserva, name="reserva"),

]