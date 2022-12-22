# Generated by Django 4.1.4 on 2022-12-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0002_request_to_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request_to_chat',
            old_name='username',
            new_name='name1',
        ),
        migrations.AddField(
            model_name='request_to_chat',
            name='name2',
            field=models.CharField(default='none', max_length=100),
        ),
    ]