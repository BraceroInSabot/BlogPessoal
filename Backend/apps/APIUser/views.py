from typing import Type
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import Response, APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from apps.core.default_response import default_response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from .serializers import RegistroUsuarioSerializer
from rest_framework.permissions import AllowAny

class RegisterTokenView(APIView):
    permission_classes = [AllowAny] #type: ignore
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request):
        """
        Create a new user.

        Args:
            request: user request
        
        Returns:
            HttpResponse: Response to the request
        """
        print(type(request))
        serializer = RegistroUsuarioSerializer(data=request.data) 

        if serializer.is_valid():                
            serializer.save()

            response: Response = Response(
                status=HTTP_201_CREATED,
                data=default_response(
                success=True, 
                message="Usuário cadastrado com sucesso!"
                )
            )
            
            return response

        return Response(
            status=HTTP_400_BAD_REQUEST,
            data=default_response(
            success=False, 
            message="Não foi possível cadastrar o seu usuário.", 
            data=serializer.errors))
