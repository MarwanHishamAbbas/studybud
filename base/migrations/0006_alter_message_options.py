# Generated by Django 4.1.4 on 2022-12-18 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_room_participents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
