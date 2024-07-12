from rest_framework.serializers import ModelSerializer
from .models import Category, Question


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


class QuestionSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Question
        fields = '__all__'
