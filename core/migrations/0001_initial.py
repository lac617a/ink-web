# Generated by Django 2.2 on 2021-06-12 00:42

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brName', models.CharField(help_text='Identifique la marca', max_length=100, unique=True, verbose_name='Nombre de la marca')),
                ('brUpdate', models.DateTimeField(auto_now_add=True)),
                ('brCreate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgName', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre de la categoria')),
                ('cgUpdate', models.DateTimeField(auto_now_add=True)),
                ('cgCreate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slBusiness', models.CharField(max_length=50, verbose_name='Nombre de la empresa')),
                ('slTypeDoc', models.CharField(choices=[('Nit', 'Nit'), ('Cédula', 'Cedula'), ('Otro', 'Otro')], default='Nit', max_length=6, verbose_name='Tipo de documento')),
                ('slNumberDoc', models.IntegerField(unique=True, verbose_name='Numero del Dcumento')),
                ('slBusinessPhone', models.IntegerField(verbose_name='Numero telefonico de la empresa')),
                ('slBusinessUrl', models.URLField(blank=True, help_text='No es requerido', unique=True, verbose_name='Sitio web de la empresa')),
                ('slUpdate', models.DateTimeField(auto_now_add=True)),
                ('slCreate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdCode', models.IntegerField(help_text='Es requerido', unique=True, verbose_name='Codigo del producto')),
                ('pdName', models.CharField(max_length=100, verbose_name='Nombre del pruducto')),
                ('pdPrice', models.DecimalField(decimal_places=3, help_text='Tome en cuenta el precio adecuado para su producto', max_digits=100000, verbose_name='Precio de venta')),
                ('pdDescription', ckeditor.fields.RichTextField(verbose_name='Descripcion del producto')),
                ('pdStock', models.IntegerField(default=0)),
                ('pdImage', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d', verbose_name='Cargar una imagen para el producto')),
                ('pdUpdate', models.DateTimeField(auto_now_add=True)),
                ('pdCreate', models.DateTimeField(auto_now_add=True)),
                ('pdBrand', models.ForeignKey(blank=True, help_text='Este campo es requerido', on_delete=django.db.models.deletion.CASCADE, to='core.Brands', verbose_name='Marca del producto')),
                ('pdCategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category', verbose_name='Categoria relacionada con el producto')),
                ('pdLikes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('pdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-id'],
            },
        ),
    ]
