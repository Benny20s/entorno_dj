# Generated by Django 4.2.1 on 2023-07-07 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0002_alter_producto_id_alter_producto_tipo_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompra',
            fields=[
                ('id_carrito', models.UUIDField(default=uuid.UUID('72aaa23a-415e-44bf-afd9-b63ebc016f88'), primary_key=True, serialize=False)),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado', models.CharField(choices=[('FINALIZADO', 'FINALIZADO'), ('PENDIENTE', 'PENDIENTE')], default='PENDIENTE', max_length=15)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='ElementoCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=0, default=1, max_digits=3)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.carritocompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carritocompra',
            name='productos',
            field=models.ManyToManyField(through='aplicacion.ElementoCarrito', to='aplicacion.producto'),
        ),
    ]