from rest_framework import serializers as s


class MoveSerializer(serizalizers.ModelSerizalizer):
	tutorial = s.Boolean
