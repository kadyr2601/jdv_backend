from django.urls import path
from homepage import views
from homepage.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),
]