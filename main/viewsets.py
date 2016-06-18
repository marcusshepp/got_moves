from rest_framework import viewsets

from main import serializers
from main import models

class DefaultCategoryViewset(viewsets.ModelViewSet):
    """

    """
    queryset = models.DefaultCategory.objects.all()
    serializer_class = serializers.DefaultCategorySerializer
    permission_classes = ()


class ClassicMoveViewset(viewsets.ModelViewSet):
    """

    """
    queryset = models.ClassicMove.objects.all()
    serializer_class = serializers.ClassicMoveSerializer
    permission_classes = ()
