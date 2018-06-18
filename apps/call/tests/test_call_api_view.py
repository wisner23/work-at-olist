from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..views import CallApi
from ..models import Call, CallRecord

class TestCallApiView(TestCase):

    def setUp(self):
        self.client = APIRequestFactory()
        self.uri = '/call/'
        self.view = CallApi.as_view()

    def test_call_api_with_start_call_should_return_201(self):
        data = self.default_payload()
        response = self.send_post(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_call_api_end_without_start_should_return_400(self):
        data = self.default_payload()
        data.update({ 'type' : CallRecord.END })
        response = self.send_post(data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, b'{"non_field_errors": ["There\'s no call registered to this call_id."]}')

    def test_call_api_end_with_start_should_return_201(self):
        AMOUNT_CALL_SHOULD_BE_CREATED = 1 
        AMOUT_CALL_RECORD_SHOULD_BE_CREATED = 2 

        data = self.default_payload()

        response_start = self.send_post(data)
        self.assertEqual(response_start.status_code, status.HTTP_201_CREATED)

        data.update({'id': 2, 'type' : CallRecord.END, 'timestamp': '2017-12-12T15:17:13Z' })        
        response = self.send_post(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        call_count = Call.objects.all().count()
        call_record_count = CallRecord.objects.all().count()

        self.assertEqual(call_count, AMOUNT_CALL_SHOULD_BE_CREATED)
        self.assertEqual(call_record_count, AMOUT_CALL_RECORD_SHOULD_BE_CREATED)

    def default_payload(self):
        data = { 
            "id":  1,
            "type": CallRecord.START, 
            "timestamp":  "2017-12-12T15:07:13Z", 
            "call_id":  1, 
            "source":  "16997563362", 
            "destination":  "16997666666" 
        }

        return data  

    def send_post(self, payload):
        request = self.client.post(self.uri, data=payload, format='json')        
        response = self.view(request)
        return response