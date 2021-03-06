# Generated by Django 2.1.2 on 2018-10-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20181018_1116'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='employee',
            name='types',
            field=models.CharField(default='student', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mail',
            field=models.CharField(max_length=320),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
