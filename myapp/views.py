from django.shortcuts import render
from django.http import HttpResponse


def encode_test(request):
    return render(request, "myapp/index.html")