# Generated by Django 3.0.5 on 2021-05-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectionApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
