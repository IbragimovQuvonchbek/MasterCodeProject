from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Client
from .serializer import ClientSerializer
from rest_framework.response import Response


class GetClientAPIView(APIView):
    def get(self, request):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        if username and password:
            clients = Client.objects.filter(username=username, password=password)
            if clients.exists():
                serializer = ClientSerializer(clients, many=True)
                return Response(serializer.data)
            return Response({"message": "incorrect password or username"})
        return Response({"message": "username or password not given"})

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "incorrect data"})
