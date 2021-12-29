# Generated by Django 3.2.4 on 2021-07-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinamo', '0002_rename_player_team_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponcor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('teams', models.ManyToManyField(to='dinamo.Team')),
            ],
        ),
    ]
