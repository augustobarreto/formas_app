from rest_framework import viewsets
from rest_framework.response import Response
from formas_app.apps.dptoie.DPTOie.predict import predict


class DPTOieViewSet(viewsets.ViewSet):
    
    def create(self, request):
        
        message = request.data['message']
        
        list_of_out = predict(message)

        if not list_of_out:
            list_of_out = "Não foi possível realizar extração para a setença"
       
        return Response({'result': list_of_out })
