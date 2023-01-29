from rest_framework import serializers
from .models import Singer, Music, MyLikeMusic, MyLikeSinger, FollowsSinger, MyPlayListMusic
from customuser.models import CustomUser

class UserList(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name']

# class SingerCreateSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Singer
#         fields = '__all__'

class MusicForSingerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'musicname', 'mp3', 'language']

class SingerListForMyLikeSingerSerializers(serializers.ModelSerializer):
    user = UserList(read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'user']

class MyLikeSingerSerializer(serializers.ModelSerializer):
    singer = SingerListForMyLikeSingerSerializers()
    class Meta:
        model = MyLikeSinger
        fields = ['id', 'singer']

class MyLikeCreateSingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLikeSinger
        fields = ['singer']


class LikeSingerForSingerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyLikeSinger
        fields = ['id']

# class FollowsSingerListSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = FollowsSinger
#         fields = ['id']

class SingerListSerializers(serializers.ModelSerializer):
    user = UserList(read_only=True)
    # musics = MusicForSingerListSerializers(source='author_musics', many=True)
    # follows = FollowsSingerListSerializers(source='follow_singer', many=True)
    class Meta:
        model = Singer
        fields = ['id', 'user', 'descriptions']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count_musics'] = instance.author_musics.count()
        representation['followers'] = instance.follow_singer.count()
        representation['likes'] = instance.singer_like.count()
        return representation

class SingerRetriveSerializers(serializers.ModelSerializer):
    user = UserList(read_only=True)
    musics = MusicForSingerListSerializers(source='author_musics', many=True)
    # follows = FollowsSingerListSerializers(source='follow_singer', many=True)
    class Meta:
        model = Singer
        fields = ['id', 'user', 'descriptions', 'musics']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['followers'] = instance.follow_singer.count()
        representation['likes'] = instance.singer_like.count()
        return representation

class SingerListForMusicSerializers(serializers.ModelSerializer):
    user = UserList(read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'user']

class MusicCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ['id', 'musicname', 'mp3', 'language']


class MusicListSerializers(serializers.ModelSerializer):
    author = SingerListForMusicSerializers(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'author', 'musicname', 'mp3', 'data_created', 'language']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.like_for_music.count()
        representation['count'] = Music.objects.count()

        return representation

class MoreLikeMusicListSerializers(serializers.ModelSerializer):
    author = SingerListForMusicSerializers(read_only=True)
    class Meta:
        model = Music
        fields = ['id', 'author', 'musicname', 'mp3', 'data_created', 'language']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.like_for_music.count()
        return representation

class FollowSingerCreateSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = FollowsSinger
        fields = ['singer']

class FollowSingerListSerilaizers(serializers.ModelSerializer):
    singer = SingerListForMyLikeSingerSerializers()
    class Meta:
        model = Singer
        fields = ['id', 'singer']

class MyLikeMusicCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyLikeMusic
        fields = ['music']

class MyLikeMusicListSerializers(serializers.ModelSerializer):
    music = MusicListSerializers(read_only=True)
    class Meta:
        model = MyLikeMusic
        fields = ['id', 'music']


class SingerCreateSerializer(serializers.ModelSerializer):
    # user =  
    class Meta:
        model = Singer
        fields = ['id', 'descriptions']

class MyPlayListMusicCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyPlayListMusic
        fields = ['music']

class MyPlayListMusicListSerializers(serializers.ModelSerializer):
    music = MusicListSerializers(read_only=True)
    class Meta:
        model = MyPlayListMusic
        fields = ['id', 'music']