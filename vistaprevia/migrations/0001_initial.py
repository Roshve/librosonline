# Generated by Django 3.2.5 on 2021-10-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(verbose_name='Fecha de publicación')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='producto/%Y/%m/%d')),
                ('categoria', models.ManyToManyField(to='vistaprevia.Categoria')),
            ],
        ),
    ]
