from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Singer, Music , MyLikeMusic, MyLikeSinger, FollowsSinger, MyPlayListMusic
# Register your models here.



@admin.register(Singer)
class SingerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'descriptions']
    list_display_links = list_display
    search_fields = ('user__username',)

    # def logo_tag(self, obj):
    #     if obj.logo:
    #         return mark_safe(f'<img src="{obj.logo.url}" width="50" height="50" />')

    # logo_tag.short_description = 'Image'


# class ProductImageInline(admin.StackedInline):
#     model = ProductImages
#     extra = 0


@admin.register(Music)
class MusicsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'musicname', 'data_created', 'language']
    list_display_links = list_display
    search_fields = ('musicname',)

    # def image_tag(self, obj):
    #     if obj.image:
    #         return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
    #
    # image_tag.short_description = 'Image'


@admin.register(MyLikeSinger)
class MyLikeSingerModelAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = list_display
    # search_fields = ('singer__name__username',)

    # def image_tag(self, obj):
    #     if obj.product.image.url:
    #         return mark_safe(f'<img src="{obj.product.image.url}" width="50" height="50" />')
    #
    # image_tag.short_description = 'Image'


@admin.register(MyLikeMusic)
class MyLikeMusicModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'music', 'like_time']
    search_fields = ['music__musicname']
    list_display_links = list_display

#     # def image_tag(self, obj):
#     #     if obj.product.image.url:
#     #         return mark_safe(f'<img src="{obj.product.image.url}" width="50" height="50" />')
#     #
#     # image_tag.short_description = 'Image'

@admin.register(FollowsSinger)
class FollowSingerModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'singer']
    list_display_links = list_display

@admin.register(MyPlayListMusic)
class MyPlayListMusicModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'music']
    list_display_links = list_display