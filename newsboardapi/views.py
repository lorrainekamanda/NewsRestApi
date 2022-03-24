from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email = email).first()

        if user is None:
            raise  AuthenticationFailed('User Not Found')

        if not user.check_password(password):
            raise  AuthenticationFailed('Incorrect Password')

        return Response({
            "message":"success"
        })

