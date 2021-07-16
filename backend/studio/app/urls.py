from django.urls import path

from . import views
from .models import *

urlpatterns = [
    path('case/', views.CaseListView.as_view()),
    path('review/', views.ReviewListView.as_view()),
    path('review/post', views.ReviewCreateView.as_view()),
]