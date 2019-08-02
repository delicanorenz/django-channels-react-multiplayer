# Generated by Django 2.1.7 on 2019-07-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0023_auto_20190706_2208")]

    operations = [
        migrations.AlterField(
            model_name="move",
            name="action_type",
            field=models.CharField(
                choices=[
                    ("post_selfie", "Post a selfie"),
                    ("post_group_selfie", "Post group selfie"),
                    ("post_story", "Post a story"),
                    ("go_live", "Go live"),
                    ("leave_comment", "Leave a comment"),
                    ("dont_post", "Don't post"),
                    ("no_move", "No move"),
                ],
                default="dont_post",
                max_length=200,
            ),
        )
    ]
