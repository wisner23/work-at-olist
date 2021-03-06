# Generated by Django 2.0.6 on 2018-06-15 18:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('destination', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='CallRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(1, 'start'), (2, 'end')])),
                ('timestamp', models.DateTimeField()),
                ('call', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.Call')),
            ],
        ),
    ]
