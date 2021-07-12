from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class CaseModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Case
        fields = ('id', 'name', 'url', 'img')


class CaseHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Case
        fields = ('id', 'name', 'url', 'img')


class CaseListSerializer(serializers.ListSerializer):

    class Meta:
        model = Case
        fields = ('id', 'name', 'url', 'img')


