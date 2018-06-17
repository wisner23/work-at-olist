from rest_framework import serializers
from ..models import Call, CallRecord

class CallStartSerializer(serializers.ModelSerializer):
    call_id = serializers.IntegerField(source="call.id")
    source = serializers.CharField(source="call.source", min_length=10)
    destination = serializers.CharField(source="call.destination", min_length=10)

    class Meta:
        model = CallRecord
        fields = [
            'id',
            'type',
            'timestamp',
            'call_id',
            'source',
            'destination'
        ]
        
    def create(self, validated_data):
        call = Call.objects.create(**validated_data['call'])
        validated_data.pop('call')

        return CallRecord.objects.create(**validated_data, call=call) 
