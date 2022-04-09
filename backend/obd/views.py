from django.shortcuts import render
from django.http import HttpResponse
from . import get_data

import obd

def get_obd(request):
    data = get_data.get_data()
    return HttpResponse(data)

# get DTC codes

# removed codes - POST?

# install a backup camera and send images