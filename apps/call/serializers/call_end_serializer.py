from rest_framework import serializers
from django.http import Http404
from django.db import transaction
from ..models import Call, CallRecord


class CallEndSerializer(serializers.ModelSerializer):

    call_id = serializers.IntegerField(source='call.id')
    
    class Meta:
        model = CallRecord
        fields = [
            'id',
            'type',
            'timestamp',
            'call_id'
        ]

    def validate(self, data):

        call = self.get_call_or_null(data['call']['id'])
        max_number_of_callrecords_peer_call = 2

        if not call:
            raise serializers.ValidationError("There's no call registered to this call_id.")

        if call.callrecord_set.count() == max_number_of_callrecords_peer_call:
            raise serializers.ValidationError('This call its already finished.')

        return data

    @transaction.atomic
    def create(self, validated_data):
        call = self.get_call_or_null(validated_data['call']['id'])
        validated_data['call'] = call

        return CallRecord.objects.create(**validated_data)

    def get_call_or_null(self, call_id):
        try:
            return Call.objects.get(pk=call_id)
        except Call.DoesNotExist:
            return None
    
    def is_timestamp_valid(self, call, timestamp):
        call_record = call.callrecord_set.first()
        