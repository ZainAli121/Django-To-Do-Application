# Generated by Django 4.2.2 on 2023-08-18 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]