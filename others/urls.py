from django.urls import path
from others.views import ContactPageView, FeedbackView

urlpatterns = [
    path('send-email', FeedbackView.as_view()),
    path('contact', ContactPageView.as_view()),
]