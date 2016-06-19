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
    Endpoint that allows for searching those classic Moves.
    by:
    - name: `/classic_move_search?name=ch`
    - description: ??
    - likes: ??
    """
    serializer_class = serializers.ClassicMoveSerializer
    def get_queryset(self):
        queryset = models.ClassicMove.objects.all()
        name_filterer = self.request.query_params.get("name", None)
        if name_filterer is not None:
            queryset = queryset.filter(name__icontains=name_filterer)
        return queryset[:5]


class ClassicMovePerformanceViewset(viewsets.ModelViewSet):
    """

    """
    queryset = models.ClassicMovePerformance.objects.all()
    serializer_class = serializers.ClassicMovePerformanceSerializer
    permission_classes = ()
