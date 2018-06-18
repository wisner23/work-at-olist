from django.db import models
from django.core.validators import MinLengthValidator


class Call(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=12, validators=[MinLengthValidator(10)])
    destination = models.CharField(max_length=12, validators=[MinLengthValidator(10)])
    

class CallRecord(models.Model):
    START = 'start'
    END = 'end'

    _CALL_RECORD_TYPES = (
        (START, 'START'),
        (END, 'END')
    ) 

    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10, choices=_CALL_RECORD_TYPES, default=START)
    timestamp = models.DateTimeField()
    call = models.ForeignKey(Call, on_delete=models.CASCADE) 
