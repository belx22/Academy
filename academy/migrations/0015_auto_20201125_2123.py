# Generated by Django 3.1.3 on 2020-11-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0014_auto_20201125_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='DateCreationCours',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
