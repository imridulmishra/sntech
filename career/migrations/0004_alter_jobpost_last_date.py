# Generated by Django 4.2.1 on 2023-05-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0003_jobpost_category_jobpost_qualification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='last_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
