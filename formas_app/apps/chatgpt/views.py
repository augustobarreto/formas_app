from rest_framework import viewsets
from rest_framework.response import Response
import openai
import requests
import os

#Enter valide OpenAPI Key
openai.api_key = os.environ.get('OPENAI_KEY')


class ChatGPTViewSet(viewsets.ViewSet):
    
    def create(self, request):
        message = request.data['message']
        endpoint = 'https://api.openai.com/v1/engines/gpt-3.5-turbo/completions'

        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai.api_key}'
        }
        
        data = {
        'prompt': (f"Pode extrair triplas no formato (Arg1, Rel, Arg2) da seguinte frase para mim? : {message}"),
        'max_tokens': 50 
        }   

        response = requests.post(endpoint, headers=headers, json=data)
        response_json = response.json()
        list_of_responses = []
        print(response_json)
        for response in response_json.get("choices"):
            list_of_responses.append(response.get("text"))


        return Response({'result': list_of_responses})
