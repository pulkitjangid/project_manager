# Generated by Django 3.1.7 on 2021-05-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_message_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='Upload',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
