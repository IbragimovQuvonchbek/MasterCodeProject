from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ResultQuestions
from client.models import Client
from questions.models import Question
from .serializers import ResultSerializer
from django.shortcuts import get_object_or_404
from uuid import uuid4
from subprocess import check_output
from json import load
import os


class CheckResultAPIView(APIView):
    def post(self, request, pk):
        username = request.data.get('username')
        solution = request.data.get('solution')

        if not username or not solution:
            return Response({"message": "username or solution not provided"}, status=400)

        is_solved = True
        is_correct = False

        client = get_object_or_404(Client, username=username)
        question = get_object_or_404(Question, pk=pk)

        file_name = f"{uuid4()}.py"
        file_path = os.path.join('check_solutions_folder', file_name)

        try:
            with open(file_path, 'w') as f:
                f.write(solution)
        except Exception as e:
            return Response({"message": f"Error writing to file"}, status=500)

        solution_file_name = f"{question.name}.py"
        solution_file_path = os.path.join('problem_solutions_folder', question.name, solution_file_name)

        jsonpath = os.path.join('problem_solutions_folder', question.name, f'{question}.json')
        with open(jsonpath, 'r') as file:
            inputs = load(file)
        correct_answer_count = 0

        try:

            for input_detail in inputs:
                result_of_server = check_output(["python", solution_file_path], input=input_detail['input'], text=True,
                                                timeout=1000)
                result_of_client = check_output(["python", file_path], input=input_detail['input'], text=True,
                                                timeout=1000)
                if result_of_server == result_of_client:
                    correct_answer_count += 1
            if correct_answer_count == len(inputs):
                is_correct = True

        except Exception as e:
            return Response({"message": f"Internal error1"}, status=500)

        try:
            os.remove(file_path)
        except Exception as e:
            return Response({"message": f"Error deleting file"}, status=500)

        result_client = ResultQuestions.objects.create(
            client=client,
            questions=question,
            solution=solution,
            is_solved=is_solved,
            is_correct=is_correct
        )

        return Response({"message": "correct" if is_correct else "incorrect"}, status=200)


class GetQuestionResult(APIView):
    def get(self, request, pk):
        username = request.query_params.get('username')
        question = get_object_or_404(Question, id=pk)
        clients = get_object_or_404(Client, username=username)

        result = ResultQuestions.objects.filter(questions=question, client=clients)

        serializer = ResultSerializer(result, many=True)
        return Response(serializer.data)
