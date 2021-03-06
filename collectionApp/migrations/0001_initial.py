# Generated by Django 3.0.5 on 2021-05-02 11:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('genres', models.ManyToManyField(blank=True, to='collectionApp.Genres')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_uuid', models.UUIDField(blank=True, default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('movies', models.ManyToManyField(blank=True, to='collectionApp.Movies')),
            ],
        ),
    ]
