# Generated by Django 3.0.6 on 2020-08-05 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answersalternatives',
            options={'ordering': ['orderansweralternatives']},
        ),
        migrations.AlterModelOptions(
            name='assessmentparameter',
            options={'ordering': ['idassessmentparameter']},
        ),
        migrations.AlterModelOptions(
            name='concept',
            options={'ordering': ['idconcept']},
        ),
        migrations.AlterModelOptions(
            name='informationitem',
            options={'ordering': ['idinformationitem']},
        ),
        migrations.AlterModelOptions(
            name='informationitemtype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='instrucelementtype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='instructionalelement',
            options={'ordering': ['idinstructionalelement']},
        ),
        migrations.AlterModelOptions(
            name='knowledgedomain',
            options={'ordering': ['idknowledgedomain']},
        ),
        migrations.AlterModelOptions(
            name='mediatype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='mobilemedia',
            options={'ordering': ['idmobilemedia']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['idmodule']},
        ),
        migrations.AlterModelOptions(
            name='phaseprocedure',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='priorknowledge',
            options={'ordering': ['idpriorknowledge']},
        ),
        migrations.AlterModelOptions(
            name='priorlevel',
            options={'ordering': ['idpriorlevel']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['orderquestion']},
        ),
        migrations.AlterModelOptions(
            name='questiontype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='range',
            options={},
        ),
        migrations.AlterModelOptions(
            name='reference',
            options={},
        ),
        migrations.AlterModelOptions(
            name='referencetype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='resolutionquestion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='scopo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='single',
            options={},
        ),
        migrations.AlterModelOptions(
            name='typethreshold',
            options={},
        ),
    ]
