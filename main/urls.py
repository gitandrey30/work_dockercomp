from django.urls import path

from main.views import get_main, get_queryset_from_database

urlpatterns=[
    path('', get_main),
    path('', get_queryset_from_database),
]