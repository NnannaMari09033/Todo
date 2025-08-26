from rest_framework import serializers
from .models import Todo, Project, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created']

class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = [
            'id', 'title', 'notes', 'completed', 'priority',
            'due_date', 'recurrence', 'metadata', 'project', 'tags',
            'created', 'modified_at'
        ]
