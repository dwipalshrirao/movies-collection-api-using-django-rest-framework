from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
# Create your views here.
import requests
from requests.auth import HTTPBasicAuth

from .serializers import Coll_serializer,MoviesSerializer
from .models import Collection,Movies
from rest_framework import viewsets


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


class Collection_view(APIView):
    serializer_class= Coll_serializer
    queryset=Collection.objects.all()
    # permission_classes = [IsstaffOrReadOnly]

    def get(self,request):
        query=Collection.objects.all()
        seri=self.serializer_class(query,many=True)
        # print(seri.data)
        # if seri.is_valid():
        return Response(seri.data)
        # return Response({'err':'rr'})





# from  rest_framework.mixins import RetrieveModelMixin,ListModelMixin
# class Collection_view(ListAPIView,RetrieveUpdateDestroyAPIView):
#     serializer_class= Coll_serializer
#     queryset=Collection.objects.all()
#     # permission_classes = [IsstaffOrReadOnly]
#     lookup_field = 'collection_uuid'


# class Collection_view(ListModelMixin,RetrieveModelMixin):
#     serializer_class= Coll_serializer
#     queryset=Collection.objects.all()
#     # permission_classes = [IsstaffOrReadOnly]
#     lookup_field = 'collection_uuid'


class movieV(viewsets.ModelViewSet):
    lookup_field='uuid'
    queryset=Movies.objects.all()
    serializer_class=MoviesSerializer
    def list(self, request):
        mov=Movies.objects.all()
        serializer=MoviesSerializer(mov,many=True)
        return Response(serializer.data)

    def retrieve(self, request,uuid=None):
        if uuid:
            mov=Movies.objects.get(uuid=uuid)
            serializer=MoviesSerializer(mov)
            return Response(serializer.data)
    
    def create(self, request):
        data=request.data
        # print((data))
        seri=MoviesSerializer(data=data)
        # data=seri.create(data)
        # print(data)
        # super(movieV, self).create(request)
        if seri.is_valid():
            print('is valid',seri.validated_data)
            seri.save()
        print('================',seri.data)
        return Response(seri.data) #['uuid']from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
# Create your views here.
import requests
from requests.auth import HTTPBasicAuth

from .serializers import Coll_serializer,MoviesSerializer
from .models import Collection,Movies
from rest_framework import viewsets


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


# class Collection_view(APIView):
#     serializer_class= Coll_serializer
#     queryset=Collection.objects.all()
#     # permission_classes = [IsstaffOrReadOnly]

#     def get(self,request):
#         query=Collection.objects.all()
#         seri=self.serializer_class(query,many=True)
#         # print(seri.data)
#         # if seri.is_valid():
#         return Response(seri.data)
#         # return Response({'err':'rr'})





# from  rest_framework.mixins import RetrieveModelMixin,ListModelMixin
class Collection_view(RetrieveUpdateDestroyAPIView):
    serializer_class= MoviesSerializer
    queryset=Movies.objects.all()
    # permission_classes = [IsstaffOrReadOnly]
    lookup_field = 'uuid'


# class Collection_view(ListModelMixin,RetrieveModelMixin):
#     serializer_class= Coll_serializer
#     queryset=Collection.objects.all()
#     # permission_classes = [IsstaffOrReadOnly]
#     lookup_field = 'collection_uuid'


class movieV(viewsets.ModelViewSet):
    lookup_field='uuid'
    queryset=Movies.objects.all()
    serializer_class=MoviesSerializer
    # def list(self, request):
    #     mov=Movies.objects.all()
    #     serializer=MoviesSerializer(mov,many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request,uuid=None):
    #     if uuid:
    #         mov=Movies.objects.get(uuid=uuid)
    #         serializer=MoviesSerializer(mov)
    #         return Response(serializer.data)
    
    def create(self, request):
        data=request.data
        seri=MoviesSerializer(data=data)
   
        # super(movieV, self).create(request)
        print(seri.is_valid())
        if seri.is_valid():
            print('is valid',seri.validated_data)
            seri.save()
            response=seri.data
        else:
            response=seri.errors
        return Response(response) #['uuid']


class CollectionView(viewsets.ModelViewSet):
    lookup_field='collection_uuid'
     
    queryset=Collection.objects.all()
    serializer_class=Coll_serializer

    def create(self, request):
        data=request.data
        seri=serializer_class(data=data)
   
        # super(movieV, self).create(request)
        print(seri.is_valid())
        if seri.is_valid():
            print('is valid',seri.validated_data)
            seri.save()
            response=seri.data
        else:
            response=seri.errors
        return Response(response) #['uuid']
