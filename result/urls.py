from django.urls import path
from .views import CheckResultAPIView, GetQuestionResult

urlpatterns = [
    path('check/<int:pk>/', CheckResultAPIView.as_view(), name='check-answer'),
    path('get-result/<int:pk>/', GetQuestionResult.as_view(), name='get-question-result'),
]
