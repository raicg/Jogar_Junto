# Generated by Django 2.1.5 on 2019-02-04 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_message_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message_chat',
            old_name='message',
            new_name='text',
        ),
    ]
