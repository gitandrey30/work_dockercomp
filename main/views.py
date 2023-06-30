from django.shortcuts import render

from main.models import Turbocharge


def get_main(request):
    return render(request, 'main.html')


def get_queryset_from_database(request):
    query = Turbocharge.objects.all()
    return render(request, query, "request_page.html")
