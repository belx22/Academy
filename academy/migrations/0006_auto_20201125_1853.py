# Generated by Django 3.1.3 on 2020-11-25 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_enseignant_nomcours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='NomCours',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academy.cours'),
        ),
    ]
