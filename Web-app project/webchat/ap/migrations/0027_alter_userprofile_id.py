# Generated by Django 3.2.10 on 2022-09-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0026_posts_retweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
