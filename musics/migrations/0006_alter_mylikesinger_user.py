# Generated by Django 4.1.2 on 2022-12-16 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musics', '0005_alter_mylikesinger_singer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylikesinger',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
