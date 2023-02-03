from django.db import models
from customuser.models import CustomUser
from django.core.validators import FileExtensionValidator

# Create your models here.


class Singer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    descriptions = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = ("Singer")
        verbose_name_plural = ("Singers")

class MyLikeSinger(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='singer_like')

    def __str__(self):
        return self.singer.user.username

    class Meta:
        verbose_name = ("MyLikeSinger")
        verbose_name_plural = ("MyLikeSingers")
        unique_together = ('user', 'singer',)

class Music(models.Model):
    MUSIC_LANGUAGE = [
    ('russian', 'russian'),
    ('uzbek', 'uzbek'),
    ('tadjik', 'tadjik'),
    ('kazak', 'kazak'),
    ('kavkaz', 'kavkaz')
    ]
    author = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='author_musics')
    musicname = models.CharField(max_length=50)
    mp3 = models.FileField(upload_to='musics', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    data_created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=50, choices=MUSIC_LANGUAGE, default=MUSIC_LANGUAGE[0])

    def __str__(self):
        return self.musicname
    
    class Meta:
        verbose_name = ("Music")
        verbose_name_plural = ("Musics")
        ordering = ('-data_created',)

        

class MyLikeMusic(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    like_time = models.DateTimeField(auto_now_add=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='like_for_music')

    def __str__(self):
        return self.music.musicname

    class Meta:
        verbose_name = ("MyLikeMusic")
        verbose_name_plural = ("MyLikeMusics")
        ordering = ('-like_time',)
        unique_together = ['user', 'music']

class MyPlayListMusic(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    like_time = models.DateTimeField(auto_now_add=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='my_play_list')

    def __str__(self):
        return self.music.musicname

    class Meta:
        verbose_name = ("MyPlayListMusic")
        verbose_name_plural = ("MyPlayListMusic")
        ordering = ('-like_time',)
        unique_together = ['user', 'music']


class FollowsSinger(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='follow_singer')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = ("FollowsSinger")
        verbose_name_plural = ("FollowsSingers")
        unique_together = ['user', 'singer']