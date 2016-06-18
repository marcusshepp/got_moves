from rest_framework import serializers as s

from main import models


class DefaultCategorySerializer(s.ModelSerializer):
    class Meta:
        model = models.DefaultCategory
        fields = (
            "name",
			"description",
			"date_created",
			"date_updated",
            "description",
            "one_handed",
            "number_of_packets",
        )


class UserSubmittedCategorySerializer(s.ModelSerializer):
    class Meta:
        model = models.DefaultCategory
        fields = (
            "name",
			"description",
			"date_created",
			"date_updated",
            "description",
            "one_handed",
            "number_of_packets",
            "user",
        )


class ClassicMoveSerializer(s.ModelSerializer):
	class Meta:
		model = models.ClassicMove
		fields = (
			"name",
			"description",
			"date_created",
			"date_updated",
			"credits",
			"category",
			"estimated_creation_date",
			# "submitted_by",
		)


class ClassicMovePerformanceSerializer(s.ModelSerializer):
	class Meta:
		model = models.ClassicMovePerformance
		fields = ('move',)
