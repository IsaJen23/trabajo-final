# Generated by Django 4.2.5 on 2023-09-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='FixMe'),
            preserve_default=False,
        ),
    ]