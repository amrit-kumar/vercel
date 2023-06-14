# example/views.py
from datetime import datetime

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.http.response import JsonResponse


@api_view(['GET'])
def getWazirxData(request):
    url = 'https://api.wazirx.com/api/v2/tickers'
    if request.method == 'GET':
        response = requests.get(url)
        return JsonResponse(response.json(),status=status.HTTP_200_OK, safe=True)

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)