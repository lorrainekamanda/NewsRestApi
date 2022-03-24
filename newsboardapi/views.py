from django.shortcuts import render
from rest_framework.views import APIView
from .models import User,Post,Comment
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed,PermissionDenied
import jwt
import datetime
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, mixins

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

        payload ={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes = 60),
            'iat':datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret',algorithm ='HS256')
        response = Response()
        response.set_cookie(key='jwt',value = token,httponly = True)

        response.data={
            "jwt":token,
            'name': user.name,
            'email': user.email
        }

        return response

def is_authenticated(request, *args, **kwargs):
    token = request.COOKIES.get('jwt')
    if not token:
        return False
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = User.objects.filter(id=payload.get('id')).first()
        request.user = user

    except jwt.ExpiredSignatureError:
        return False

    return True


def is_permission_allowed(request, obj, *args, **kwargs):
    return obj.author == request.user

class PostApiView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
       
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        request.data['author'] = request.user.id
        return self.create(request, *args, **kwargs)
