# Generated by Django 2.1.7 on 2019-06-27 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190625_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameplayer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='game',
            name='game_players',
        ),
        migrations.AlterField(
            model_name='message',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='app.Game'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='GamePlayer',
        ),
    ]
