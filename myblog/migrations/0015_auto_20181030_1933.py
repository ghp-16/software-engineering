# Generated by Django 2.1.2 on 2018-10-30 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_interview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='team_name',
            new_name='team',
        ),
    ]
