# Generated by Django 5.0.2 on 2024-05-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_projectdetails_url_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='hear_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.IntegerField()),
                ('message', models.TextField(max_length=100)),
            ],
        ),
    ]
