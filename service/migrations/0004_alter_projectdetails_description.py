# Generated by Django 5.0.2 on 2024-04-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_projectdetails_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
