from django.urls import path
from .views import GetAllCategoryAPIView, GetAllQuestionsAPIView, GetQuestionDetailAPIView

urlpatterns = [
    path('get-categories/', GetAllCategoryAPIView.as_view(), name='get-all-categories'),
    path('get-questions/', GetAllQuestionsAPIView.as_view(), name='get-all-questions'),
    path('get-questions/<int:pk>/', GetQuestionDetailAPIView.as_view(), name='get-question-detail')
]
