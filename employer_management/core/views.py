from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import Employer
from .serializers import UserSerializer, RegisterSerializer, EmployerSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': UserSerializer(user).data,
                'message': 'User registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        User = get_user_model().objects.filter(email=email).first()
        
        if User and User.check_password(password):
            refresh = RefreshToken.for_user(User)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class EmployerListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployerSerializer
    
    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class EmployerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployerSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)
    

class APIRootView(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome to the Employer Management API",
            "endpoints": {
                "signup": "/api/auth/signup/",
                "login": "/api/auth/login/",
                "profile": "/api/auth/profile/",
                "employers": "/api/employers/",
            }
        })
        
class RootView(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome to the Employer Management System",
            "api": "Visit /api/ for the API endpoints"
        })