# Generated by Django 4.1.4 on 2023-01-08 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0004_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_to_chat',
            name='name1',
        ),
        migrations.AddField(
            model_name='request_to_chat',
            name='acceptor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meet.profile'),
        ),
    ]