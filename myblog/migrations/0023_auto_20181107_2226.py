# Generated by Django 2.1.2 on 2018-11-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0022_auto_20181107_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='choose',
            field=models.CharField(default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='employee',
            name='txted',
            field=models.CharField(default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='interview',
            name='judge_list',
            field=models.CharField(default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='interview',
            name='student_list',
            field=models.CharField(default='', max_length=4000),
        ),
    ]
