from django.urls import path
from projects.views import ProjectsPageView, ProjectsGalleryView

urlpatterns = [
    path('', ProjectsPageView.as_view(), name='projects'),
    path('details/<slug>', ProjectsGalleryView.as_view(), name='gallery'),
]