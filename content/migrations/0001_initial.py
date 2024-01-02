# Generated by Django 5.0 on 2023-12-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_user_nickname', models.CharField(max_length=30)),
                ('feed_number', models.IntegerField()),
                ('comment_text', models.TextField()),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('content_image', models.CharField(max_length=200)),
                ('content_text', models.TextField()),
                ('heart_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Contents',
            },
        ),
    ]
