from rest_framework import serializers
from .models import AudioFile


class TextToSpeechSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioFile
        fields = '__all__'
