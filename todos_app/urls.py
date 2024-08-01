from django.urls import path
from .views import *


urlpatterns = [
    path('api/', TodosAPIView.as_view()),
    path('api/<int:pk>/', TodosUpdateAPIView.as_view()),
    path('api/delete/<int:pk>/', TodosDeleteAPIView.as_view()),
]
