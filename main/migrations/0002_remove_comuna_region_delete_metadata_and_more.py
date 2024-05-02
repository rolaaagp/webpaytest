# Generated by Django 4.2.11 on 2024-05-01 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna',
            name='region',
        ),
        migrations.DeleteModel(
            name='Metadata',
        ),
        migrations.RemoveField(
            model_name='productofotos',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='productorecomendados',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
        migrations.RemoveField(
            model_name='usersmetadata',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='usersmetadata',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='usersmetadata',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='usersmetadata',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='usersmetadata',
            name='perfiles',
        ),
        migrations.RemoveField(
            model_name='usersmetadata',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='carrito',
            options={},
        ),
        migrations.AlterModelOptions(
            name='ordendecompra',
            options={},
        ),
        migrations.AlterModelOptions(
            name='ordendecompradetalle',
            options={},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={},
        ),
        migrations.RemoveField(
            model_name='ordendecompra',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='ordendecompra',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_antes',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='producto_categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='sku',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='slug',
        ),
        migrations.AlterField(
            model_name='carrito',
            name='users_metadata',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ordendecompra',
            name='users_metadata',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Pais',
        ),
        migrations.DeleteModel(
            name='Perfiles',
        ),
        migrations.DeleteModel(
            name='ProductoCategoria',
        ),
        migrations.DeleteModel(
            name='ProductoFotos',
        ),
        migrations.DeleteModel(
            name='ProductoRecomendados',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.DeleteModel(
            name='UsersMetadata',
        ),
    ]