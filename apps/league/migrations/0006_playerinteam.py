# Generated by Django 2.1.5 on 2019-01-25 13:48

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.TeamSeason')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
