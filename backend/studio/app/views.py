from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render


from .serializer import *
from .models import Case, Review


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CaseListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    


