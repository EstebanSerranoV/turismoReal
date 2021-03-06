# Generated by Django 3.2.7 on 2021-10-23 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acompaniante',
            fields=[
                ('id_acomp', models.FloatField(primary_key=True, serialize=False)),
                ('cantidad', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'acompaniante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_admi', models.FloatField(primary_key=True, serialize=False)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_carg', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('detalle_cargo', models.CharField(max_length=200)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id_chin', models.FloatField(primary_key=True, serialize=False)),
                ('detalle_entrega', models.CharField(max_length=150)),
                ('pago_pendiente', models.CharField(max_length=150)),
                ('ingreso_conformidad', models.CharField(max_length=150)),
                ('hora_chin', models.DateTimeField()),
                ('fecha_chin', models.DateField()),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'check_in',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id_chou', models.FloatField(primary_key=True, serialize=False)),
                ('estado_entrega', models.CharField(max_length=50)),
                ('multas_out', models.CharField(max_length=50)),
                ('pagos_multas_out', models.CharField(max_length=50)),
                ('hora_chou', models.DateTimeField()),
                ('fecha_chou', models.DateField()),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'check_out',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_clie', models.FloatField(primary_key=True, serialize=False)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comu', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id_cond', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('correo', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'conductor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_depa', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('info_departamento', models.CharField(max_length=150)),
                ('servicio_asociado', models.CharField(max_length=150)),
                ('entorno_departamento', models.CharField(max_length=150)),
                ('tarifa', models.BigIntegerField()),
                ('condicion_uso', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_dire', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_calle', models.CharField(max_length=150)),
                ('numero_calle', models.IntegerField()),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id_edificio', models.FloatField(primary_key=True, serialize=False)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'edificio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id_func', models.FloatField(primary_key=True, serialize=False)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'funcionario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InformeGanancia',
            fields=[
                ('id_inga', models.FloatField(primary_key=True, serialize=False)),
                ('ganancia_departamento', models.BigIntegerField()),
                ('ganancia_zona', models.BigIntegerField()),
                ('ganancia_diaria', models.BigIntegerField()),
                ('ganancia_semanal', models.BigIntegerField()),
                ('ganancia_anual', models.BigIntegerField()),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'informe_ganancia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InformeReserva',
            fields=[
                ('id_inre', models.FloatField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'informe_reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inve', models.FloatField(primary_key=True, serialize=False)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'inventario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mantenimeinto',
            fields=[
                ('id_mant', models.FloatField(primary_key=True, serialize=False)),
                ('amoblado', models.CharField(max_length=150)),
                ('cable', models.CharField(max_length=100)),
                ('calefaccion', models.CharField(max_length=150)),
                ('internet', models.CharField(max_length=100)),
                ('mantenimiento', models.CharField(max_length=100)),
                ('otros_servicios', models.CharField(max_length=100)),
                ('disponibilidad', models.CharField(max_length=50)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'mantenimeinto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_prov', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_regi', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_rese', models.FloatField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('pago_porcentaje', models.BigIntegerField()),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.FloatField(primary_key=True, serialize=False)),
                ('tipo_rol', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServicioExtra',
            fields=[
                ('id_servex', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'servicio_extra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServicioTransporte',
            fields=[
                ('id_setr', models.FloatField(primary_key=True, serialize=False)),
                ('lugar_transporte', models.CharField(max_length=150)),
                ('horario_transporte', models.DateTimeField()),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'servicio_transporte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id_tour', models.FloatField(primary_key=True, serialize=False)),
                ('lugar_tour', models.CharField(max_length=30)),
                ('hora_tour', models.DateField()),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'tour',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usua', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('rut', models.CharField(max_length=12)),
                ('correo', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_vehi', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('patente', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=100)),
                ('estado', models.FloatField()),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.ImageField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'felicitaciones']], upload_to='')),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
