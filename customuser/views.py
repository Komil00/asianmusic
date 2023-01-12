from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from .serializers import CustomUserSerializers, CustomUserVerifySerializer, CustomUserListSerializer
from .models import CustomUser

from rest_framework import permissions

from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     if obj.author == request.user:
    #         return True
    #     return False


class UsersViewList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['email', 'username']
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer

# class UserView(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#
#     def perform_update(self, serializer):
#         if self.request.user.is_staff:
#             instance = self.get_object()
#             serializer.save(instance=instance)
#         if self.request.user.role == 'MANAGER':
#             user = CustomUser.objects.get(pk=self.kwargs['pk'])
#             if user.role == 'OPERATOR':
#                 instance = self.get_object()
#                 serializer.save(instance=instance)
#             else:
#                 return None


# class AccountView(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = AccountSerializer

class UsersVerifyApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = CustomUserVerifySerializer(data=data)
        if serializer.is_valid():
            email = serializer.data['email']
            code = serializer.data['code']
            user = CustomUser.objects.filter(email=email)
            if not user.exists():
                return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data' : 'invalid email'
                })
            if user.first().code != code:
                return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data' : 'invalid code' 
                })
            user = user.first()
            user.is_verify = True
            user.save()

            return Response({
                'status' : 200,
                'message' : 'account verified',
                'data' : {} 
                })
