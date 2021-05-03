
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Movies,Genres,Collection
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # depth = 2


class StringGenreField(serializers.StringRelatedField):

    def to_internal_value(self, value):
        print(value)
        genre=Genres.objects.get_or_create(name=value)
        return genre[0]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['name']

from uuid import UUID

class MoviesSerializer(serializers.ModelSerializer):
    genres = StringGenreField(many=True,required=False)
   
    class Meta:
        model = Movies
        fields = ['uuid', 'title', 'genres', 'description']




    def validate(self,data):
        uuid=data.get('uuid','')
        if uuid == '':
            raise serializers.ValidationError({'uuid':'uuid must be provided'})

        if not data.get('title'):
            raise serializers.ValidationError("movie title not provided")
        
        return data
        

    





class Coll_serializer(serializers.ModelSerializer):
    # movies = StringMoviesField(many=True)
    movies = MoviesSerializer(many=True)
    uuid= serializers.ReadOnlyField()

    
    class Meta:
        model = Collection
        fields = ['uuid', 'title', 'description', 'movies']
        extra_kwargs = {"title": {
                                    "error_messages": {"required": "collection title must be provided"}
                                    },
                         
                            }

    def create(self, validated_data):
        print('seri',validated_data)
        movies=[]
        if validated_data.get('movies'):
            movies=validated_data.pop('movies')

        movie_objects=[]

        title=validated_data.get('title','')
        description=validated_data.get('description','')

        collection=Collection.objects.create(title=title,description=description)
        for data in movies:
           
            genre=data.pop('genres')
            title=data.get('title','')
            description=data.get('description','')
            movie=Movies.objects.create(collection_id=collection.uuid, **data) #title=title,description=description
            if genre:
                print(genre,'genre')
                movie.genres.set(genre)
       
            movie_objects.append(movie)

        collection.movies.set(movie_objects)

        user = self.context.get("request")
        collection.user=user
        collection.save()

       
        return collection


    def update(self, instance, validated_data):

        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        
        movies=validated_data.get('movies','')
       
        if not movies:
            instance.save()
            return instance       
        else:
            movie_objs=[]
            for i in movies:
               
                genres=i.pop('genres')
                movie=Movies.objects.get_or_create(uuid=i.get('uuid'),collection_id=instance.uuid)

                if movie[1]:
                    movie[0].title=i.get('title',movie[0].title)
                    movie[0].description=i.get('description',movie[0].description)
                else:
                    movie[0].title=i.get('title','')
                    movie[0].description=i.get('description','')
                movie[0].save()
                movie[0].genres.set(genres)
                movie_objs.append(movie[0])
            instance.movies.set(movie_objs)
        
        return instance


    