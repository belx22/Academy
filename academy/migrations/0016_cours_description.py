# Generated by Django 3.1.3 on 2020-11-25 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0015_auto_20201125_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
