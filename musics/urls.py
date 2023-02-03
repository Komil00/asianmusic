from django.urls import path, include
from rest_framework import routers
from .views import SingerListView, MusicListViewSet,\
     LikeForSingerViewSet, FollowForSingerViewSet, MyLikeMusicViewSet,\
        SingerCreateViewSet, MusicCreateViewSet, MoreLikeMusicViewSet,\
            MyPlayListMusicViewSet

router = routers.DefaultRouter()
router.register(r'list_singers', SingerListView, basename='list_singers')
router.register(r'create_singers', SingerCreateViewSet, basename='create_singers')
router.register(r'my_like_singer', LikeForSingerViewSet, basename='my_like_singer')
router.register(r'my_follow_singer', FollowForSingerViewSet, basename='my_follow_singer')

router.register(r'create_musics', MusicCreateViewSet, basename='create_musics')
router.register(r'musics', MusicListViewSet, basename='musics')
router.register(r'more_like_musics', MoreLikeMusicViewSet, basename='more_like_musics')
router.register(r'my_like_musics', MyLikeMusicViewSet, basename='my_like_musics')
router.register(r'my_playlist', MyPlayListMusicViewSet, basename='my_playlist')



urlpatterns = [
    path('', include(router.urls))
]