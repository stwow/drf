import self as self
from django.db.migrations import serializer
from django.shortcuts import render, redirect

from django.views import generic
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView
from dinamo.serializers import *
from dinamo.models import *


class ShowPlayers(generic.ListView):
    model = Team
    template_name = 'dinamo/all_players.html'

    def post(self, request):
        print(request.POST)
        result = list()
        player = Players.objects.filter(name=request.POST['name_players'])
        for i in player:
            a = Team.objects.filter(players_id=i.pk)
            result.append(a[0].title)
        print(result)
        context = {"result": result}
        return render(request, 'dinamo/all_players.html', context)

class ShowStadium(APIView):

    def get(self,request):
        stad = Stadium.objects.all()
        serializer = StadiumSerializer(stad, many=True)
        return Response(serializer.data)


class AllShow(APIView):

    def get(self, request):
        stadium = Stadium.objects.all()
        players = Players.objects.all()
        team = Team.objects.all()
        sponcor = Sponcor.objects.all()
        serializer = PlayersSerializer(players, many=True)
        serializer2 = StadiumSerializer(stadium, many=True)
        serializer3 = TeamSerializer(team, many=True)
        serializer4 = SponcorSerializer(sponcor, many=True)
        res = {'stadium': serializer2.data, 'players':serializer.data, 'team': serializer3.data, 'sponcor': serializer4.data}
        return Response(res)

class PlayerView(APIView):

    def get(self,request, pk=None):
        if not pk:
            players = Players.objects.all()
            serializer=PlayersSerializer(players, many=True)
        else:
            player = Players.objects.get(pk=pk)
            serializer = PlayersSerializer(player)
        return Response(serializer.data)

    def post(self,request):
        serializer = PlayersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        player = Players.objects.get(pk=pk)
        serializer = PlayersSerializer(player, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class GetPlayerGeneric(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayerModelSerializer

    def fn(self):
        return self.queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer =self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PlayerViewSet(viewsets.ViewSet):

    def list(sel,request):
        queryset = Players.objects.all()
        serializer = PlayerModelSerializer(queryset, Many=True)
        return Response(serializer.data)

    def retrive(self,request, pk=None):
        queryset = Players.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = PlayerModelSerializer(user)
        return Response(serializer.data)

player_list = PlayerViewSet.as_view({'get':'list'})
player_list_r = PlayerViewSet.as_view({'get': 'retrive'})
