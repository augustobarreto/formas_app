from rest_framework import viewsets, serializers
from rest_framework.response import Response
from formas_app.apps.oie.OIE.predict import Predictor
from drf_yasg.utils import swagger_auto_schema

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()


class PTOIEFlairViewSet(viewsets.ViewSet):
    
    @swagger_auto_schema(request_body=MessageSerializer)
    def create(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            predictor = Predictor(model="best-model")
            output = predictor.pred(message, show_output=False)
           
            return Response({'result': output })
        else:
            return Response(serializer.errors, status=400)
