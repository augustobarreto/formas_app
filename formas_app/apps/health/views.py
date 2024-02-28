from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


class HealthCheckView(APIView):
    def get(self, request):
        
        """
        Permite checar se a aplicação está disponível.
        """
        content = {'status': 'ok'}
        return Response(content)
