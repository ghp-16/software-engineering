# Generated by Django 2.1.2 on 2018-10-29 02:42

from django.db import migrations
import myblog.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_team_captain_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='choose',
            field=myblog.fields.ListField(default='123456789'),
        ),
    ]
