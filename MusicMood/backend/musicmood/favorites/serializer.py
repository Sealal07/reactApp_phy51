from .models import FavoriteTrack
from rest_framework import serializers

class FavoriteTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTrack
        fields = '__all__'