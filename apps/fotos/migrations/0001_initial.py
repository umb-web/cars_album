# Generated by Django 5.1.6 on 2025-02-22 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mifoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
                ('descripcion', models.CharField(max_length=2000)),
                ('imageurl', models.CharField(max_length=120)),
                ('publish', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
