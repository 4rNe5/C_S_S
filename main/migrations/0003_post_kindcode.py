# Generated by Django 4.2.2 on 2023-06-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='kindcode',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
