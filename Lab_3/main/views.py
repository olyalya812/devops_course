from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime

def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    time = datetime.now()
    response = {'date': time.strftime("%Y-%m-%d %H:%M:%S"),
                'storinka': request.build_absolute_uri(),
                'infa_pro_server': os.uname(),
                'infa_pro_clienta': request.headers['User-Agent']}
    return JsonResponse(response)
