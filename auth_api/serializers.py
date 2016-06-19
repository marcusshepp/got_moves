from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}
    )
    password_two = serializers.CharField(
        style={"input_type": "password"},
        read_only=True
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password_two",
        )

    def create(self, validated_data):
        if validated_data.get("password", "") == validated_data.get("password_two", ""):
            validated_data.pop("password_two")
            user = User(
                username = validated_data.get("username", None),
                password = validated_data.get("password", None)
            )
            user.save()
            return user
