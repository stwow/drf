# Generated by Django 3.2.4 on 2021-07-04 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinamo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='player',
            new_name='players',
        ),
    ]
