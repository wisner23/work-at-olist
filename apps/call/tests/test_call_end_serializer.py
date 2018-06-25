from django.test import TestCase
from ..serializers import CallEndSerializer
from ..models import Call, CallRecord
from rest_framework import serializers

class TestCallEndSerializer(TestCase):

    def setUp(self):
        self.data = self.data_payload()
        self.save_start_call()

    def test_create_should_persist_call(self):
        AMOUNT_CALL_SHOULD_BE_CREATED = 1
        AMOUNT_CALL_RECORD_SHOULD_BE_CREATED = 2 

        serializer = CallEndSerializer(data=self.data)

        self.assertTrue(serializer.is_valid())
        serializer.save()

        call_record_count = CallRecord.objects.all().count()
        call_count = Call.objects.all().count()

        self.assertEqual(call_record_count, AMOUNT_CALL_RECORD_SHOULD_BE_CREATED)
        self.assertEqual(call_count, AMOUNT_CALL_SHOULD_BE_CREATED)

    def test_create_end_with_call_doesnt_exist_should_except(self):
        data = self.data
        data['call_id'] = 2
        serializer = CallEndSerializer(data=data)

        with(self.assertRaises(serializers.ValidationError)):
            serializer.is_valid(raise_exception=True)

    def test_end_call_thats_already_finished_should_except(self):
        serializer = CallEndSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        second_serializer = CallEndSerializer(data=self.data)
        with(self.assertRaises(serializers.ValidationError)):
            second_serializer.is_valid(raise_exception=True)


    def data_payload(self):
        data = {
            'id': 2,
            'type': CallRecord.END,
            'timestamp': '2017-12-12T15:17:13Z',
            'call_id': 1
        }
        
        return data

    def save_start_call(self):
        
        call = Call.objects.create(source='16997563362', destination='16997563362', id=1)
        CallRecord.objects\
            .create(
                id = 1, 
                type = 1,
                call = call,
                timestamp = '2017-12-12T15:07:13Z'
            )

        