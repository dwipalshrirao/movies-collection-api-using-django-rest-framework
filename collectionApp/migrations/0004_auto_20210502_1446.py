# Generated by Django 3.0.5 on 2021-05-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectionApp', '0003_auto_20210502_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
