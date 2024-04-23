
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import requests



# Create your views here.

@api_view(["GET", "POST"])
def user_list(request):
    url = 'https://dev.codeleap.co.uk/careers/'
    if request.method == 'GET':
        resposta = requests.get(url)
        if resposta.status_code == 200:
            data = resposta.json()
            data_json = json.dumps(data['results'])
            results = json.loads(data_json)
            return Response(results)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'POST':

        data = json.loads(request.body)



        try:
            resposta = requests.post(url, json=data)
            resposta.raise_for_status()
            return Response(resposta.json())
        except requests.exceptions.HTTPError as err:
            return Response(err.response.json(), status=err.response.status_code)



@api_view(["DELETE", "PATCH"])
def user_detail(request, id):
    url = f'https://dev.codeleap.co.uk/careers/{id}/'

    if request.method == 'DELETE':
        resposta = requests.delete(url) 
        if resposta.status_code == 204:
            #print("success")
            return Response("Success ", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)   

    elif request.method == 'PATCH':
        data = json.loads(request.body) 

        try:
            resposta = requests.patch(url, json=data)
            resposta.raise_for_status()
            return Response(resposta.json())
        except requests.exceptions.HTTPError as err:
            return Response(err.response.json(), status=err.response.status_code)



