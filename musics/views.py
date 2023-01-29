from django.shortcuts import render
from .models import Singer, Music, MyLikeMusic, MyLikeSinger, FollowsSinger, MyPlayListMusic
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.db.models import Avg, Max, Min, Sum, Count
# from .tasks import notification
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .serilaizers import SingerListSerializers, SingerRetriveSerializers,\
     MusicListSerializers, MyLikeSingerSerializer, MyLikeCreateSingerSerializer,\
    FollowSingerListSerilaizers, FollowSingerCreateSerilaizers, MyLikeMusicListSerializers,\
        MyLikeMusicCreateSerializers, SingerCreateSerializer, MusicCreateSerializers,\
            MoreLikeMusicListSerializers, MyPlayListMusicListSerializers, MyPlayListMusicCreateSerializers


# Create your views here.

class SingerCreateViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerCreateSerializer
    authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = SingerCreateSerializer(data=request.data)
        if request.user.who == 'Singer':
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save(user=self.request.user)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response('There is a singer with this user')
        else:
            return Response('At the time of registration, you have established yourself as a listener. You can change your role by accessing your profile to eliminate', status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Singer.objects.filter(user=self.request.user) 


class SingerListView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerListSerializers
    authentication_classes = [IsAuthenticated]
    http_method_names = ['get', 'retrive']
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['author_musics__data_created']
    search_fields = ['user__username']
    authentication_classes = [SessionAuthentication]
    # notification.delay()
        
    def get_serializer_class(self):
        if self.action in ['list']:
            return SingerListSerializers
        else:
            return SingerRetriveSerializers

class LikeForSingerViewSet(ModelViewSet):
    queryset = MyLikeSinger.objects.all()
    serializer_class = MyLikeSingerSerializer
    authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # ordering_fields = ['author_musics__data_created']
    # search_fields = ['user__username']
    authentication_classes = [SessionAuthentication]

    def get_serializer_class(self):
        if self.action == 'create':
            return MyLikeCreateSingerSerializer
        return MyLikeSingerSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = MyLikeCreateSingerSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user) # user pole ni zapros berayotgan user bn tuldiradi
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(f"{request.user.first_name} You have clicked like to this Singer", status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        return MyLikeSinger.objects.filter(user=self.request.user)

class FollowForSingerViewSet(ModelViewSet):
    queryset = FollowsSinger.objects.all()
    serializer_class = FollowSingerListSerilaizers
    authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # ordering_fields = ['author_musics__data_created']
    # search_fields = ['user__username']
    authentication_classes = [SessionAuthentication]

    def get_serializer_class(self):
        if self.action == 'create':
            return FollowSingerCreateSerilaizers
        return FollowSingerListSerilaizers

    def create(self, request, *args, **kwargs):
        try:
            serializer = FollowSingerCreateSerilaizers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user) # user pole ni zapros berayotgan user bn tuldiradi
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(f"{request.user.first_name} You have followed to this Singer", status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        return FollowsSinger.objects.filter(user=self.request.user)

class MusicCreateViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicCreateSerializers
    authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def create(self, request, *args, **kwargs):
        if request.user.who in ["Singer"]:
            singer = Singer.objects.get(user=self.request.user)
            serializer = MusicCreateSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(author=singer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('At the time of registration, you have established yourself as a listener. You can change your role by accessing your profileto eliminate', status=status.HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        return Music.objects.filter(author__user=self.request.user)


class MusicListViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicListSerializers
    authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['musicname', 'author__user__username', 'language']
    http_method_names = ['get']


class MyLikeMusicViewSet(ModelViewSet):
    queryset = MyLikeMusic.objects.all()
    serializer_class = MyLikeMusicListSerializers
    authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['musicname', 'author__user__username', 'language']
    authentication_classes = [SessionAuthentication]

    def get_serializer_class(self):
        if self.action == 'create':
            return MyLikeMusicCreateSerializers
        return MyLikeMusicListSerializers

    def create(self, request, *args, **kwargs):
        try:
            serializer = MyLikeMusicCreateSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user) # user pole ni zapros berayotgan user bn tuldiradi
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(f"{request.user.first_name} You have liked to this Music", status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        return MyLikeMusic.objects.filter(user=self.request.user)


class MoreLikeMusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MoreLikeMusicListSerializers
    authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['musicname', 'author__user__username', 'language']
    authentication_classes = [SessionAuthentication]
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        queryset = Music.objects.select_related('like_for_music').all()
        serializer = MoreLikeMusicListSerializers(queryset, many=True)
        return Response(serializer.data)

# from django.core.mail import send_mail
# from django.conf import settings

# def send(email):
# 	send_mail(
#             subject='Add an eye-catching subject',
    		# message='Komil chtu',
    		# from_email=settings.EMAIL_HOST_USER,
    		# recipient_list=[email])
# from .tasks import send_spam_email

class MyPlayListMusicViewSet(ModelViewSet):
    queryset = MyPlayListMusic.objects.all()
    serializer_class = MyPlayListMusicCreateSerializers
    authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    authentication_classes = [SessionAuthentication]

    def get_serializer_class(self):
        if self.action == 'create':
            return MyPlayListMusicCreateSerializers
        return MyPlayListMusicListSerializers

    def create(self, request, *args, **kwargs):

        try:
            serializer = MyPlayListMusicCreateSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            # send_spam_email.delay(request.user.email)
            serializer.save(user=self.request.user) # user pole ni zapros berayotgan user bn tuldiradi
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(f"{request.user.first_name} You after added this Music to your PlayList", status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        return MyPlayListMusic.objects.filter(user=self.request.user)
