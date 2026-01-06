from rest_framework import serializers
from catalogo.models import Juego

class JuegoSerializer(serializers.ModelSerializer):
    
    imagen = serializers.ImageField(
        required=False,
        allow_null=True
    )

    class Meta:
        model = Juego
        fields = "__all__"
