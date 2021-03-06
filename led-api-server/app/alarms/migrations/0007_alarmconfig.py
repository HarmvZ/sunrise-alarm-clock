# Generated by Django 3.1.2 on 2020-10-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarms', '0006_auto_20191003_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colors', models.JSONField(help_text='List of colors to progress through')),
                ('playlist', models.CharField(blank=True, help_text='Mopidy URI of playlist', max_length=255)),
                ('volumes', models.JSONField(help_text='List of (time, volume) tuples to progress through')),
                ('duration', models.IntegerField(help_text='Duration of wake up cycle in seconds')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
    ]
