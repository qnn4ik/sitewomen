from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import *


class WomenAPIView(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
