# Generated by Django 4.0.5 on 2022-06-08 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authAPI', '0002_alter_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]