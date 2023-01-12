# Generated by Django 4.1.2 on 2023-01-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_alter_customuser_who'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]