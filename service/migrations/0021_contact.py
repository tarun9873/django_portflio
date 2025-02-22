# Generated by Django 5.0.2 on 2024-05-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_alter_hear_me_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('msg', models.TextField(max_length=100)),
            ],
        ),
    ]
