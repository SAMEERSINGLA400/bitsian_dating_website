# Generated by Django 4.1.4 on 2023-01-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0006_remove_request_to_chat_name2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_to_chat',
            name='is_accepted',
            field=models.BooleanField(null=True),
        ),
    ]
