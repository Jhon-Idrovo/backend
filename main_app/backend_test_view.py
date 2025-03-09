from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class BackendTest(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response(data={"message":"Backend working"},status=status.HTTP_200_OK)