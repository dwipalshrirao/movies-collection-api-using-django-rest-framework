# Generated by Django 3.2 on 2021-05-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectionApp', '0007_collection_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='genres',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movies',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
