# Generated by Django 4.1.4 on 2023-01-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0008_messgae_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=1000)),
                ('room', models.CharField(max_length=1000)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Messgae',
        ),
    ]
