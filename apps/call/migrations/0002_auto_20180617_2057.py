# Generated by Django 2.0.6 on 2018-06-17 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callrecord',
            name='type',
            field=models.CharField(choices=[('start', 'START'), ('end', 'END')], default='start', max_length=10),
        ),
    ]
