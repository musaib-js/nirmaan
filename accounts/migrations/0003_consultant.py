# Generated by Django 3.2.4 on 2022-04-27 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220426_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('qualification', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=300)),
                ('clinic', models.CharField(max_length=300)),
                ('contact', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
    ]
