from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests.auth import HTTPBasicAuth

from .serializers import Coll_serializer,MoviesSerializer
from .models import Collection,Movies
from django.contrib.auth import login as Login_process
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_401_UNAUTHORIZED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from collectionApp.utils import get_tokens_for_user
from django.contrib.auth.models import User
import collections

class RegisterView(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            exists = User.objects.filter(username=username)
            print(exists.exists())
            if exists.exists():
                user = User.objects.get(username=username)
                Login_process(request, user)
                token = get_tokens_for_user(user)
              
            else:
                user = User.objects.create(username=username, password=password)
                print(user)
                token = get_tokens_for_user(user)
                print(token)
                Login_process(request, user)
               
            return Response(data={'status': True, 'message': 'Authentication successfull', 'token': token['access']
                                      }, status=HTTP_200_OK) #"user": response

        except Exception as e:
            return Response(data={'status': False, 'message': 'Invalid Credential'},
                            status=HTTP_400_BAD_REQUEST)





class moivesList(APIView):
    

    def get_movies(self,page=None):
        Username='iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0'
        Password='Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'
        if page:
            url = 'https://demo.credy.in/api/v1/maya/movies/'+'?page='+page
        else:
            url = 'https://demo.credy.in/api/v1/maya/movies/'
        response = requests.get(url,auth = HTTPBasicAuth(Username, Password))
        return response

    def get(self,request):
        
        page=request.GET.get('page')
        response=self.get_movies(page=page)
        data=response.json()
        if data.get('error'):
            return Response(data,status=response.status_code)

        if data.get("next"):
            data["next"]=data['next'].replace('https://demo.credy.in/api/v1/maya','http://127.0.0.1:8000')

        if data.get("previous"):
            data["previous"]=data['previous'].replace('https://demo.credy.in/api/v1/maya','http://127.0.0.1:8000')

        return Response(data)



class CollectionView(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field='uuid' 
    queryset=Collection.objects.all()
    serializer_class=Coll_serializer


    def list(self, request):
        data=self.queryset.filter(user=request.user)
        serializer=self.serializer_class(data,many=True).data
        genres=[]
        for i in serializer:
            for movie in i.pop('movies'):
                genres.extend(movie.get('genres'))

        top_genre=collections.Counter(genres)
        fvr_genre=[i[0] for i in top_genre.most_common(3)]

        return Response({"is_success": True,"data": {
                                "collections":serializer,"favourite_genres":fvr_genre}})


    def retrieve(self,request,uuid=None,*args,**kwargs):
        try:
            data=self.queryset.get(uuid=uuid)
            
            if data.user==request.user:
                print(uuid,"------------",data)
                serializer=self.serializer_class(data).data
                print(uuid,"------------",data)
                response=serializer
                return Response(response,status=HTTP_200_OK)
            else:
                response={'uuid':'Given collection is not belongs to you so can\'t see the data'}
                return Response(response,status=HTTP_401_UNAUTHORIZED)

        except:           
            response={'uuid':'Given collection uuid is not available'}
            return Response(response,status=HTTP_404_NOT_FOUND) 


    def create(self, request):
        data=request.data
        serializer=self.serializer_class(data=data,context={'request':request.user})
   
        if serializer.is_valid():
            serializer.save()
            response=serializer.data.get('uuid')
            return Response({"uuid":response})
        else:
            response=serializer.errors
        return Response(response,status=HTTP_201_CREATED) #['movie_uuid']

    


    def update(self,request,uuid=None,*args,**kwargs):

        data=request.data
        try:
            coll_queryset= Collection.objects.get(uuid=uuid)
            print(coll_queryset.user==request.user)
            if coll_queryset.user==request.user:
                serializer=self.serializer_class(coll_queryset,data=data,partial=True)
        
                if serializer.is_valid():
                    serializer.save()
                    response=serializer.data

                    return  Response(response, status=HTTP_201_CREATED)
                else:
                    response=serializer.errors

                    return  Response(response, status=HTTP_400_BAD_REQUEST)
            else:
                response={"uuid":'Given collection is not belongs to you so can\'t make changes'}
                # status=status.HTTP_401_UNAUTHORIZED
                return Response(response,status=HTTP_401_UNAUTHORIZED)

        except:
            response={'uuid':'Given collection uuid is not available'}
            return Response(response,status=HTTP_404_NOT_FOUND)
        

    def destroy(self,request,uuid=None,*args,**kwargs):
        try:
            coll_queryset= Collection.objects.get(uuid=uuid)
            if coll_queryset.user==request.user:

                coll_queryset.delete()
                response={'your collection is deleted'}
                return Response(response,status=status.HTTP_200_OK)
            else:
                response={'uuid':'Given collection is not belongs to you so can\'t make changes'}
                return Response(response,status=HTTP_401_UNAUTHORIZED)
        except:
            response={'uuid':'Given collection uuid is not available'}
            return Response(response,status=HTTP_404_NOT_FOUND)



