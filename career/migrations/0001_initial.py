# Generated by Django 4.2.1 on 2023-05-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('jobfunction', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=20)),
                ('skills', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=30)),
                ('discription', models.CharField(max_length=200)),
            ],
        ),
    ]
