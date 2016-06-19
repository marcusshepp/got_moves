from rest_framework import serializers as s

from main import models


class MoveCategorySerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = models.MoveCategory
        fields = (
            "id",
            "name",
			"description",
			"date_created",
			"date_updated",
            "description",
            "one_handed",
            "number_of_packets",
            "detail_url",
            "time_past_since_creation",
            "url",
            # "user",
        )
        read_only_fields = (
            "time_past_since_creation",
            "detail_url",
        )


class ClassicMoveSerializer(s.ModelSerializer):
	class Meta:
		model = models.ClassicMove
		fields = (
            "id",
			"name",
			"description",
			"date_created",
			"date_updated",
			"credits",
			"category",
			"estimated_creation_date",
            "category_detail_url",
            "category_display",
            "time_past_since_creation",
			# "submitted_by",
		)


class ClassicMovePerformanceSerializer(s.ModelSerializer):
	class Meta:
		model = models.ClassicMovePerformance
		fields = (
            'id',
            'date_created',
            'date_updated',
            'upvotes',
            'description',
            'name',
            'private',
            'youtube_link',
            'instagram_link',
            'placeholder_image',
        )
