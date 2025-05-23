from rest_framework import serializers
from homepage.models import HomePage
from projects.serializers import ProjectSerializer

class HomePageSerializer(serializers.ModelSerializer):
    featured_projects = serializers.SerializerMethodField()

    class Meta:
        model = HomePage
        exclude = [
            'featured_project_wide',
            'featured_project_tall',
            'featured_project_normal',
            'featured_project_normal_second',
            'featured_project_normal_third',
            'featured_project_wide_second',
        ]
        depth = 1

    def get_featured_projects(self, obj):
        projects_with_size = [
            (obj.featured_project_wide, "wide"),
            (obj.featured_project_tall, "tall"),
            (obj.featured_project_normal, "normal"),
            (obj.featured_project_normal_second, "normal"),
            (obj.featured_project_normal_third, "normal"),
            (obj.featured_project_wide_second, "wide"),
        ]

        serialized_projects = []
        for project, size in projects_with_size:
            data = ProjectSerializer(project).data
            data['size'] = size
            serialized_projects.append(data)
        return serialized_projects