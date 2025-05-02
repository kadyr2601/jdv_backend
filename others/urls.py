from django.urls import path
from others.views import SEOView, FeedbackView

urlpatterns = [
    path('send-email', FeedbackView.as_view(), name='feedback'),
    path('seo/<str:page>', SEOView.as_view(), name='seo'),
]