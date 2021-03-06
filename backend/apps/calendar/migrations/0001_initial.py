# Generated by Django 3.1.4 on 2021-09-27 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000)),
                ('eventType', models.IntegerField(choices=[(0, 'Ưu tiên cao'), (1, 'Ưu tiên Trung bình'), (2, 'Ưu tiên thấp')], default=2)),
                ('startTime', models.DateField()),
                ('endTime', models.TimeField()),
                ('description', models.CharField(max_length=1000)),
                ('user_control', models.ManyToManyField(related_name='user_control_set', to=settings.AUTH_USER_MODEL)),
                ('user_room', models.ManyToManyField(related_name='user_room_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('startTime', 'endTime')},
            },
        ),
    ]
