# Generated by Django 3.1.3 on 2020-12-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0017_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='NomCours',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]