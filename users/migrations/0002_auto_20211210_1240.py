# Generated by Django 3.2.4 on 2021-12-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cedula',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='telefono',
            field=models.CharField(max_length=200),
        ),
    ]
