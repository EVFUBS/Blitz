# Generated by Django 4.0.5 on 2022-06-09 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionAPI', '0002_answer_correct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=200)),
                ('group_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionAPI.group'),
        ),
    ]
