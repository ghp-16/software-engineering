# Generated by Django 2.1.2 on 2018-10-28 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20181021_0036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.AddField(
            model_name='employee',
            name='grade',
            field=models.CharField(default='大一', max_length=5),
        ),
        migrations.AddField(
            model_name='employee',
            name='major',
            field=models.CharField(default='计算机系', max_length=15),
        ),
        migrations.AddField(
            model_name='employee',
            name='number',
            field=models.CharField(default='2016011123', max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='student_name',
            field=models.CharField(default='暂无', max_length=20),
        ),
    ]
