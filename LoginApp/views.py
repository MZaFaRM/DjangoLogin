from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import LoginSerializer
from rest_framework import status

class LoginViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def login(self, request):
        return Response({'data':'login'})

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # check if user and password are correct
            if serializer.validated_data['user'] == 'aswin' and serializer.validated_data['password'] == '1234':
                return Response({'status': 'success'})
            else:
                return Response({'status': 'Invalid login'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
