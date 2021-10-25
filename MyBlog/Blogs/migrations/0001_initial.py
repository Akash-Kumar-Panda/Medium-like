# Generated by Django 3.2.6 on 2021-08-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='def', max_length=255)),
                ('content', models.TextField()),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
