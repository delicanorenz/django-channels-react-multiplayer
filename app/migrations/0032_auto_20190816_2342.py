# Generated by Django 2.1.7 on 2019-08-16 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("app", "0031_auto_20190816_2300")]

    operations = [
        migrations.RenameField(
            model_name="gameplayer", old_name="stories", new_name="selfies"
        )
    ]