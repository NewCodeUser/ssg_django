from django.urls import path
from.views import encode_test

urlpatterns = [
    path("", encode_test),
]