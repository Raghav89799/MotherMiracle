from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):

    def post(self,request):
        user_data = request.data
        print(user_data)

        ser = RegisterSerializer(data = user_data)
        ser.is_valid(raise_exception=True)
        ser.save()

        return Response({
            'message':'data is successfully registered',
        })
    
    def put(self,request,pk):

        data = request.data
        instance = MyUser.objects.get(pk=pk)
        serializers = RegisterSerializer(instance=instance,data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        instance.set_password(data['password'])
        instance.save()
        return Response({"Message" : "Data updated successfully"})
    

class LoginView(APIView):

    def post(self,request):

        data = request.data
        email = data['email']
        password = data['password']
        try:
            user = authenticate(email=email,password=password)
            print(user)
            if user is not None:
                token = get_tokens_for_user(user)
            else:
                token = None
                return Response({"Message" : "User is invalid!"})
            return Response({"Message" : token})
        except:
            return Response({"Message" : "error occured!"})

