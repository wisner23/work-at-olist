from django.test import TestCase
from ..serializers import CallStartSerializer 
from ..models import Call, CallRecord

class TestCallStartSerializer(TestCase):

    def setUp(self):
        self.data = self.data_payload()

    def test_start_call_should_persist_call(self):
        AMOUT_CALL_SHOULD_BE_CREATED = 1
        serializer = CallStartSerializer(data=self.data)
        
        self.assertTrue(serializer.is_valid())
        serializer.save()
        
        call_amount = Call.objects.all().count()
        self.assertEqual(serializer.data, self.data)
        self.assertEqual(call_amount, AMOUT_CALL_SHOULD_BE_CREATED)

    def test_start_two_call_same_id_should_throw_error(self):
        AMOUT_CALL_SHOULD_BE_CREATED = 1
        call = Call.objects.create(id=1, source='16997563362', destination='16997563362')
        
        serializer = CallStartSerializer(data=self.data)
        
        self.assertFalse(serializer.is_valid())

    def data_payload(self):
        data = { 
            "id":  1,
            "type": CallRecord.START, 
            "timestamp":  "2017-12-12T15:07:13Z", 
            "call_id":  1, 
            "source":  "16997563362", 
            "destination":  "16997666666" 
        }

        return data