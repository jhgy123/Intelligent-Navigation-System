# Generated by Django 2.2.10 on 2022-06-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
    ]
