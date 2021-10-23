# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.base import Model
from django.utils.regex_helper import Choice


class Acompaniante(models.Model):
    id_acomp = models.FloatField(primary_key=True)
    cantidad = models.BigIntegerField()
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=150)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'acompaniante'


class Administrador(models.Model):
    id_admi = models.FloatField(primary_key=True)
    estado = models.FloatField()
    id_usua = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usua')

    class Meta:
        managed = False
        db_table = 'administrador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    id_carg = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    detalle_cargo = models.CharField(max_length=200)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cargo'


class CheckIn(models.Model):
    id_chin = models.FloatField(primary_key=True)
    detalle_entrega = models.CharField(max_length=150)
    pago_pendiente = models.CharField(max_length=150)
    ingreso_conformidad = models.CharField(max_length=150)
    hora_chin = models.DateTimeField()
    fecha_chin = models.DateField()
    estado = models.FloatField()
    id_func = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_func')
    id_rese = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_rese')

    class Meta:
        managed = False
        db_table = 'check_in'


class CheckOut(models.Model):
    id_chou = models.FloatField(primary_key=True)
    estado_entrega = models.CharField(max_length=50)
    multas_out = models.CharField(max_length=50)
    pagos_multas_out = models.CharField(max_length=50)
    hora_chou = models.DateTimeField()
    fecha_chou = models.DateField()
    estado = models.FloatField()
    id_func = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_func')
    id_chin = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='id_chin')

    class Meta:
        managed = False
        db_table = 'check_out'


class Cliente(models.Model):
    id_clie = models.FloatField(primary_key=True)
    estado = models.FloatField()
    id_acomp = models.ForeignKey(Acompaniante, models.DO_NOTHING, db_column='id_acomp')
    id_usua = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usua')

    class Meta:
        managed = False
        db_table = 'cliente'



class Comuna(models.Model):
    id_comu = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    estado = models.FloatField()
    id_prov = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='id_prov')

    class Meta:
        managed = False
        db_table = 'comuna'
    
    
    def __str__(self):
        return self.nombre

class Conductor(models.Model):
    id_cond = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    correo = models.CharField(max_length=150)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conductor'


class Departamento(models.Model):
    id_depa = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    info_departamento = models.CharField(max_length=150)
    servicio_asociado = models.CharField(max_length=150)
    entorno_departamento = models.CharField(max_length=150)
    tarifa = models.BigIntegerField()
    condicion_uso = models.CharField(max_length=150)
    estado = models.FloatField()
    id_admi = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admi')
    id_edificio = models.ForeignKey('Edificio', models.DO_NOTHING, db_column='id_edificio')
    

    class Meta:
        managed = False
        db_table = 'departamento'


class Direccion(models.Model):
    id_dire = models.FloatField(primary_key=True)
    nombre_calle = models.CharField(max_length=150)
    numero_calle = models.IntegerField()
    estado = models.FloatField()
    id_comu = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comu')

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Edificio(models.Model):
    id_edificio = models.FloatField(primary_key=True)
    estado = models.FloatField()
    id_dire = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_dire')

    class Meta:
        managed = False
        db_table = 'edificio'


class Funcionario(models.Model):
    id_func = models.FloatField(primary_key=True)
    estado = models.FloatField()
    id_carg = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_carg')
    id_usua = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usua')

    class Meta:
        managed = False
        db_table = 'funcionario'


class InformeGanancia(models.Model):
    id_inga = models.FloatField(primary_key=True)
    ganancia_departamento = models.BigIntegerField()
    ganancia_zona = models.BigIntegerField()
    ganancia_diaria = models.BigIntegerField()
    ganancia_semanal = models.BigIntegerField()
    ganancia_anual = models.BigIntegerField()
    estado = models.FloatField()
    id_admi = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admi')

    class Meta:
        managed = False
        db_table = 'informe_ganancia'


class InformeReserva(models.Model):
    id_inre = models.FloatField(primary_key=True)
    detalle = models.CharField(max_length=150)
    estado = models.FloatField()
    id_admi = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admi')
    id_rese = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_rese')

    class Meta:
        managed = False
        db_table = 'informe_reserva'


class Inventario(models.Model):
    id_inve = models.FloatField(primary_key=True)
    estado = models.FloatField()
    id_depa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_depa')

    class Meta:
        managed = False
        db_table = 'inventario'


class Mantenimeinto(models.Model):
    id_mant = models.FloatField(primary_key=True)
    amoblado = models.CharField(max_length=150)
    cable = models.CharField(max_length=100)
    calefaccion = models.CharField(max_length=150)
    internet = models.CharField(max_length=100)
    mantenimiento = models.CharField(max_length=100)
    otros_servicios = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=50)
    estado = models.FloatField()
    id_depa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_depa')

    class Meta:
        managed = False
        db_table = 'mantenimeinto'


class Provincia(models.Model):
    id_prov = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    estado = models.FloatField()
    id_regi = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_regi')

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    id_regi = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'region'


class Reserva(models.Model):
    id_rese = models.FloatField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pago_porcentaje = models.BigIntegerField()
    estado = models.FloatField()
    id_clie = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_clie')
    id_admi = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admi')
    id_servex = models.ForeignKey('ServicioExtra', models.DO_NOTHING, db_column='id_servex')
    id_depa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_depa')

    class Meta:
        managed = False
        db_table = 'reserva'


class Rol(models.Model):
    id_rol = models.FloatField(primary_key=True)
    tipo_rol = models.CharField(max_length=150)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rol'


class ServicioExtra(models.Model):
    id_servex = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    estado = models.FloatField()
    id_setr = models.ForeignKey('ServicioTransporte', models.DO_NOTHING, db_column='id_setr')
    id_tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column='id_tour')

    class Meta:
        managed = False
        db_table = 'servicio_extra'


class ServicioTransporte(models.Model):
    id_setr = models.FloatField(primary_key=True)
    lugar_transporte = models.CharField(max_length=150)
    horario_transporte = models.DateTimeField()
    estado = models.FloatField()
    id_cond = models.ForeignKey(Conductor, models.DO_NOTHING, db_column='id_cond')
    id_vehi = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_vehi')

    class Meta:
        managed = False
        db_table = 'servicio_transporte'


class Tour(models.Model):
    id_tour = models.FloatField(primary_key=True)
    lugar_tour = models.CharField(max_length=30)
    hora_tour = models.DateField()
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tour'


class Usuario(models.Model):
    id_usua = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    rut = models.CharField(max_length=12)
    correo = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    estado = models.FloatField()
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculo(models.Model):
    id_vehi = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=150)
    patente = models.CharField(max_length=10)
    color = models.CharField(max_length=100)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'vehiculo'


opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.ImageField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre