# Generated by Django 4.1.5 on 2023-01-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_card',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]