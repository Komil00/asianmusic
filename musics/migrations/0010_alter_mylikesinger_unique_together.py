# Generated by Django 4.1.2 on 2022-12-17 06:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musics', '0009_remove_mylikesinger_singer_alter_mylikesinger_user_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mylikesinger',
            unique_together={('user', 'singer')},
        ),
    ]