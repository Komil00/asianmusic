# Generated by Django 4.1.2 on 2022-12-15 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0004_remove_mylikesinger_yesno_alter_mylikesinger_singer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylikesinger',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singer_like', to='musics.singer'),
        ),
    ]