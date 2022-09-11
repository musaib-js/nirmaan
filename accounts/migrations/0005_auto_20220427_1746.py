# Generated by Django 3.2.4 on 2022-04-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_consultant_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='not-specfied', max_length=6),
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default='patient', max_length=350),
        ),
    ]
