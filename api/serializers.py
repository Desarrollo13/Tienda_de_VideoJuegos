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
    def get_imagen(self, obj):
        request = self.context.get("request")
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None    
