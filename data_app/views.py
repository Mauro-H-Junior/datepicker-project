from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def date(request):
    return render(request, 'dates/date.html')

def pagina_inicial(request):
    return HttpResponse('Pronto para Investir')