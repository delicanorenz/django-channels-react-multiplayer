# Generated by Django 2.1.7 on 2019-06-10 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("app", "0005_auto_20190609_1947")]

    operations = [
        migrations.RemoveField(model_name="game", name="created_at"),
        migrations.RemoveField(model_name="game", name="updated_at"),
    ]
