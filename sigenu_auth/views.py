from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from .services import authenticate_with_aga

class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user_data = authenticate_with_aga(username, password)
        if not user_data:
            return Response({"detail": "Credenciales incorrectas o usuario bloqueado"}, status=status.HTTP_401_UNAUTHORIZED)

        # Formato que espera SIGENU
        personal = user_data["personal_information"]
        response_data = {
            "email": "",  # Si lo tienes, ponlo aquí
            "facultyId": None,
            "townUniversityId": None,
            "identification": personal["dni"],
            "lastname": personal["sn"].split(" ")[-1],
            "name": personal["given_name"],
            "role": "STUDENT",  # o "PROFESSOR", si puedes deducirlo
            "status": "ACTIVE",
            "surname": personal["sn"].split(" ")[0],
            "username": user_data["uid"]
        }

        return Response(response_data, status=status.HTTP_200_OK)
