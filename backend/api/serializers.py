"""Ok."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Ok."""

    class Meta:
        """Ok."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
