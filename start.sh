#!/bin/bash

exec gunicorn billingapi.wsgi:application --workers 3 --timeout 30 