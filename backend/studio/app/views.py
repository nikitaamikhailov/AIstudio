from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


from .serializer import *
from .models import Case, Review, Person
from .license import IsOwnerProfileOrReadOnly


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CaseListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    


class PersonListCreateView(generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    # permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]