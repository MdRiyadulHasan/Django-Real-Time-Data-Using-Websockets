# Generated by Django 4.2.4 on 2023-08-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
