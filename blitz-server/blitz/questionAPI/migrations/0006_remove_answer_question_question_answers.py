# Generated by Django 4.0.5 on 2022-06-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionAPI', '0005_group_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='questionAPI.answer'),
        ),
    ]
