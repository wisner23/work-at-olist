from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

from .serializers import CallStartSerializer, CallEndSerializer
from .models import CallRecord

class CallApi(APIView):

    serializer = CallStartSerializer

    def post(self, request):
        
        serializer = None

        if request.data['type'] == CallRecord.END:
            serializer = CallEndSerializer(data=request.data)
        else:
            serializer = CallStartSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)