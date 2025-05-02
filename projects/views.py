from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import Project, ProjectGallery, MainBanner
from projects.serializers import ProjectSerializer, MainBannerSerializer, ProjectGallerySerializer


class ProjectsPageView(APIView):
    def get(self, request):
        banner = MainBanner.objects.first()
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        return Response({'projects': projects_serializer.data,
                         'banner': MainBannerSerializer(banner).data if banner else None,
                         })




class ProjectsGalleryView(APIView):
    def get(self, request, slug):
        project = Project.objects.get(slug=slug)
        project_serializer = ProjectSerializer(project)
        gallery = ProjectGallery.objects.filter(project=project)
        serializer = ProjectGallerySerializer(gallery, many=True)
        return Response({"project": project_serializer.data, "gallery": serializer.data})
