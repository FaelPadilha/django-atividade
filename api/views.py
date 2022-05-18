from rest_framework import viewsets, permissions

from .models import Banco
from .serializers import BancoSerializer

# Create your views here.
class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    permission_classes = [permissions.IsAuthenticated]
