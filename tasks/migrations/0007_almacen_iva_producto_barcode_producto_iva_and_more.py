# Generated by Django 4.2.7 on 2023-12-09 06:52

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_cliente_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='almacen')),
            ],
            options={
                'verbose_name': 'almacen',
                'verbose_name_plural': 'almacenes',
            },
        ),
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'verbose_name': 'iva',
                'verbose_name_plural': 'iva',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='barcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='producto',
            name='porcion',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='producto',
            name='servicio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad',
            field=models.CharField(choices=[('Pieza', 'Pieza'), ('Kg', 'Kg'), ('gramos', 'gramos'), ('Lt', 'Lt'), ('Metro', 'Metro'), ('Caja', 'Caja'), ('Onza', 'Onza'), ('Charola', 'Charola'), ('Otro', 'Otro')], default='Pieza', max_length=255),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_venta',
            field=models.CharField(choices=[('Pieza', 'Pieza'), ('Kg', 'Kg'), ('gramos', 'gramos'), ('Lt', 'Lt'), ('Metro', 'Metro'), ('Caja', 'Caja'), ('Onza', 'Onza'), ('Charola', 'Charola'), ('Otro', 'Otro')], default='Pieza', max_length=255),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[100, 100], upload_to='productos'),
        ),
    ]
