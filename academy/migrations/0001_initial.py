# Generated by Django 3.1.3 on 2020-11-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomCours', models.CharField(max_length=20, unique=True)),
                ('DateCreationCours', models.DateTimeField(auto_now_add=True)),
                ('PourTousLeMonde', models.BooleanField(default=True)),
            ],
        ),
    ]
