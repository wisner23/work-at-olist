from django.conf.urls import url, include
from apps.call.urls import call_routes

API_VERSION = 'api/v1/'

api_routes = []
api_routes.extend(call_routes)

urlpatterns = [
    url(API_VERSION, include(api_routes)),
]
