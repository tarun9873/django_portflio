# Generated by Django 5.0.2 on 2024-05-04 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_myproject_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('project_image', models.ImageField(upload_to='projectdetails')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.myproject')),
            ],
        ),
    ]
