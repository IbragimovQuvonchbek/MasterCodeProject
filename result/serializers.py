from rest_framework.serializers import ModelSerializer
from .models import ResultQuestions
from questions.serializers import QuestionSerializer


class ResultSerializer(ModelSerializer):
    questions = QuestionSerializer()
    class Meta:
        model = ResultQuestions
        fields = '__all__'
