# Generated by Django 5.0.2 on 2024-05-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_hear_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hear_me',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]
