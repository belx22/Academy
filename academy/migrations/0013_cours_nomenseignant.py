# Generated by Django 3.1.3 on 2020-11-25 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0012_cours_photocours'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='NomEnseignant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academy.enseignant'),
        ),
    ]
