# Generated by Django 2.1.2 on 2018-10-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_remove_employee_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='划水队', max_length=10)),
                ('captain', models.CharField(default='可达鸭', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='mail',
            field=models.CharField(default='example@163.com', max_length=320),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default='18800137836', max_length=11),
        ),
    ]
