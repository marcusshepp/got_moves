from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters

from got_moves.settings import LOGIN_REDIRECT_URL as LRU

from main import serializers
from main import models


class MoveCategoryViewset(viewsets.ModelViewSet):
    """

    """
    queryset = models.MoveCategory.objects.all()
    serializer_class = serializers.MoveCategorySerializer
    permission_classes = ()


class ClassicMoveViewset(viewsets.ModelViewSet):
    """

    """
    queryset = models.ClassicMove.objects.all()
    serializer_class = serializers.ClassicMoveSerializer
    permission_classes = ()


class ClassicMoveFilterListView(generics.ListAPIView):
    """
    """
    queryset = models.ClassicMove.objects.all()
    serializer = serializers.ClassicMoveSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "description",
        "name",
        "credits",
        "estimated_creation_date",
        "date_created",
        "date_updated",
        "id",
    )

class ClassicMovePerformanceViewset(viewsets.ModelViewSet):
    """

    """
    queryset = models.ClassicMovePerformance.objects.all()
    serializer_class = serializers.ClassicMovePerformanceSerializer
    permission_classes = ()
