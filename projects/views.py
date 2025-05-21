from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import Project, ProjectGallery, ProjectsPage
from projects.serializers import ProjectSerializer, ProjectsPageSerializer, ProjectGallerySerializer


class ProjectsPageView(APIView):
    def get(self, request):
        page = ProjectsPage.objects.first()
        serializer = ProjectsPageSerializer(page)
        return Response(serializer.data)

class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectsGalleryView(APIView):
    def get(self, request, slug):
        project = Project.objects.get(slug=slug)
        project_serializer = ProjectSerializer(project)
        gallery = ProjectGallery.objects.filter(project=project)
        serializer = ProjectGallerySerializer(gallery, many=True)
        return Response({"project": project_serializer.data, "gallery": serializer.data})
