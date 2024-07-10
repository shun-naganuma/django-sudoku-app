from django.urls import path
from .views import SudokuView

urlpatterns = [
    path('', SudokuView.as_view()),
]
