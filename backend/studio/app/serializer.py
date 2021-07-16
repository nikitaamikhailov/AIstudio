from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReadySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ready
        fields = "__all__"
