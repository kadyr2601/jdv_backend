from django.urls import path
from services import views

urlpatterns = [
    path('interior', views.InteriorDesignServiceView.as_view()),
    path('fitout', views.FitOutServiceView.as_view()),
    path('architecture', views.ArchitectureServiceView.as_view())
]