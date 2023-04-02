from rest_framework import viewsets
from djangoapp import serializers
from djangoapp import models

class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MoviesSerializer
    queryset = models.Movies.objects.all()
