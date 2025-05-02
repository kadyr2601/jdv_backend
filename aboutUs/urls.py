from django.urls import path
from aboutUs.views import AboutUsPageView

urlpatterns = [
    path('', AboutUsPageView.as_view(), name='about'),
]