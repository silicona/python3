# Generated by Django 2.1 on 2018-08-19 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180818_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('f_alta', models.DateTimeField(auto_now=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=None, to='blog.Usuario')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog.Post')),
            ],
        ),
    ]
