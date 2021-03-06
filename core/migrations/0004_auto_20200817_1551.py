# Generated by Django 3.0.6 on 2020-08-17 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200816_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('fk_iduser', models.ForeignKey(db_column='fk_idUser', on_delete=django.db.models.deletion.CASCADE, related_name='cities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Citys',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
