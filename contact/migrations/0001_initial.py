# Generated by Django 3.2.4 on 2021-12-09 01:11

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
            name='Contac',
            fields=[
                ('id_c', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=200)),
                ('mensaje', models.CharField(max_length=200)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'contact',
                'ordering': ('id_c',),
                'managed': True,
            },
        ),
    ]
