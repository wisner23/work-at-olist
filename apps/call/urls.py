from django.conf.urls import url
from .views import CallApi

call_routes = [
    url(r'^call/$', CallApi.as_view()),
]
