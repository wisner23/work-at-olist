from rest_framework import serializers
from django.http import Http404
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
        if not self._get_or_null(data['call']['id']):
            raise serializers.ValidationError('There\'s no call registered to this call_id.')

        return data

    def create(self, validated_data):
        call = self._get_or_null(validated_data['call']['id'])
        validated_data['call'] = call

        return CallRecord.objects.create(**validated_data)

    def _get_or_null(self, call_id):
        try:
            return Call.objects.get(pk=call_id)
        except Call.DoesNotExist:
            return None