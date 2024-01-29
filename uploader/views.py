from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response

from .services import verifyUsers, createUsers, uploadFile

@api_view(['POST'])
def checkUsers(request):
    if request.method == 'POST':
        data = request.data

        user = verifyUsers(data)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'token': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['POST'])
def registerUsers(request):
    if request.method == 'POST':
        data = request.data

        result_user = createUsers(data)

        if result_user:
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'User not created'}, status=status.HTTP_500_CREATED)

    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def uploadFiles(request):
    if request.method == 'POST':

        file = uploadFile(request)

        if not file:
            return Response({'error': 'Nenhum arquivo enviado'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Arquivo recebido com sucesso'}, status=status.HTTP_200_OK)

    return Response({'error': 'Método não permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)