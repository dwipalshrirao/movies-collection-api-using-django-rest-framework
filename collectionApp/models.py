from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import User

class Genres(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return f"{self.name}"


class Movies(models.Model):
    id = models.AutoField(primary_key=True)

    collection_id=models.UUIDField(max_length=100, blank=True,null=True)
    uuid = models.UUIDField(max_length=100, blank=True, default=uuid.uuid4)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500, null=True, blank=True)
    genres = models.ManyToManyField(Genres, blank=True)

    def __str__(self):
        return f"{self.title}"


class Collection(models.Model):
    id = models.AutoField(primary_key=True)

    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    uuid = models.UUIDField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500, null=True, blank=True)
    movies = models.ManyToManyField(Movies, blank=True)

    def __str__(self):
        return f"{self.title}"
