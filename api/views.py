
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from catalogo.models import Juego
from rest_framework import viewsets,permissions
from drf_spectacular.utils import extend_schema
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import JuegoSerializer



@extend_schema(
    request=JuegoSerializer,
    responses=JuegoSerializer,
)

class JuegoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

    authentication_classes = [JWTAuthentication]
    parser_classes = [MultiPartParser, FormParser]  # 🔴 CLAVE
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plataforma']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return []




class JuegoViewSet(viewsets.ModelViewSet):
    """
    API de juegos:
    - GET: público
    - POST: solo autenticados (JWT)
    """
    queryset = Juego.objects.all().order_by('-id')
    serializer_class = JuegoSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]



class JuegoAdminViewSet(ModelViewSet):

    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ["post"]






