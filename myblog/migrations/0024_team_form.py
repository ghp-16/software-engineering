# Generated by Django 2.1.2 on 2018-11-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0023_auto_20181107_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='form',
            field=models.CharField(default='', max_length=4000),
        ),
    ]
