# Generated by Django 3.0.6 on 2020-08-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200814_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AddField(
            model_name='user',
            name='path',
            field=models.CharField(blank=True, db_column='path', max_length=256, null=True),
        ),
    ]
