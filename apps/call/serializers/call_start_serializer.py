from rest_framework import serializers
from django.db import transaction
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

    def validate(self, data):

        if self.get_call_or_null(data['call']['id']):
            raise serializers.ValidationError('The call_id its already registered.')

        if self.get_call_record_or_null(data['id']):
            raise serializers.ValidationError('The id its already registered.')

        return data

    @transaction.atomic
    def create(self, validated_data):
        call = Call.objects.create(**validated_data['call'])
        validated_data.pop('call')

        return CallRecord.objects.create(**validated_data, call=call) 

    def get_call_or_null(self, call_id):
        try:
            return Call.objects.get(pk=call_id)
        except Call.DoesNotExist:
            return None

    def get_call_record_or_null(self, record_id):
        try:
            return CallRecord.objects.get(pk=record_id)
        except CallRecord.DoesNotExist:
            return None

       


