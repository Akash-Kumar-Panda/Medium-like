# Generated by Django 3.2.6 on 2021-08-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0004_auto_20210809_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbNail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
