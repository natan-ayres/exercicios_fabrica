from rest_framework import serializers
from djangoapp import models


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movies
        fields = '__all__'