from django.urls import path
from .views import GetClientAPIView
urlpatterns = [
    path('get-client/', GetClientAPIView.as_view(), name="get-client-api")
]
