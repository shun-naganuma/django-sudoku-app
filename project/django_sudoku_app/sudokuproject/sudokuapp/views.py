from django.shortcuts import render
from django.views.generic import TemplateView

class SudokuView(TemplateView):
    template_name = 'index.html'
