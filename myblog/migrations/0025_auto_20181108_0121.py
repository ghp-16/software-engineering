# Generated by Django 2.1.2 on 2018-11-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0024_team_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='form',
            field=models.CharField(default='{"team":"军乐队","temp_list":[{"name":"才华","value":"99"},{"name":"谈吐","value":"99"},{"name":"形象","value":"100"}]}', max_length=4000),
        ),
    ]
