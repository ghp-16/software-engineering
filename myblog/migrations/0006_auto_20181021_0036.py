# Generated by Django 2.1.2 on 2018-10-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_remove_book_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.CharField(max_length=20),
        ),
    ]
