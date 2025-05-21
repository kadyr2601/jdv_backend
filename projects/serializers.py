from rest_framework import serializers
from projects.models import ProjectGallery, Project, ProjectsPage


class ProjectsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsPage
        fields = '__all__'


class ProjectGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGallery
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'