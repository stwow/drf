from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from .models import *
import json
import requests
from .serializers import *
import io


# class A:
#     def __init__(self, name, username, email):
#         self.name = name
#         self.username = username
#         self.email = email
#
#     def get_name(self):
#         return self.name
#
#
# user = requests.get('https://jsonplaceholder.typicode.com/users/1')
# print(type(user.text))
# a1 = user.json()
# print(type(a1))
# a = A(a1['name'], a1['username'], a1['email'])
# print(a.get_name())
# res = json.dumps(a.__dict__)
# d = {'id':1, 'name':'Johan'}
# _json = json.dumps(d)

@api_view(['GET', 'POST'])
def index(request):
    # confety = ProductModel.objects.all()
    # data = ProductSerializer(confety, many=True)
    # if request.method == 'POST':
    #     print(request.data)
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    # return Response(data.data)

    confeti = ProductModel.objects.all()
    data = ProductSerializerModel(confeti, many=True)
    if request.method == 'POST':
        print(request.data)
        serializer = ProductSerializerModel(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
    return Response(data.data, status=201)
    # return Response(data.data)


@csrf_exempt
@api_view(['GET', 'PUT'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = ProductModel.objects.get(pk=pk)
    except ProductModel.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProductSerializerModel(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        serializer = ProductSerializerModel(product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)


def get_object(request):
    try:
        return ProductModel.objects.all()
    except:
        return Http404


class ProductView(APIView):

    def get(self, request):
        product = get_object(request)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse_lazy('main:index'))
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class UserView(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse_lazy('main:user'))
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class CityView(APIView):

    def get(self, request):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)


class CountryView(APIView):

    def get(self, request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse_lazy('main:country'))


class MaterialView(APIView):

    def get(self, request):
        obj = Material.objects.all()
        serializer = MaterialSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = MaterialSerializer(data = request.data, many=True)
        print(request.data)
        if serializer.is_valid():
            print(serializer.validated_data, 'view')
            serializer.save()
            return Response(status=200)
        return Response(serializer.data)
