from rest_framework import serializers
from projects.models import ProjectGallery, Project, MainBanner


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'


class ProjectGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGallery
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'