from django.contrib.auth.models import User

from rest_framework import viewsets

from auth_api import serializers


class UserViewset(viewsets.ModelViewSet):
    """

    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = ()
