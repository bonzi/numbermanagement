# Generated by Django 5.0.2 on 2024-04-29 10:32

import django.db.models.deletion
import django.utils.timezone
import numman.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.PositiveIntegerField()),
                ('end', models.PositiveIntegerField()),
                ('privileged', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfService',
            fields=[
                ('name', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('privileged', models.BooleanField()),
                ('param_type', models.CharField(choices=numman.models.get_types, max_length=3)),
                ('param_length', models.SmallIntegerField()),
                ('param_name', models.CharField(max_length=32)),
                ('group_capable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('value', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=32)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('directory', models.BooleanField(choices=[(True, 'List in Public Phonebook'), (False, 'Not Listed')], default=False)),
                ('param', models.CharField(max_length=32)),
                ('barred', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('fwd_number', models.CharField(blank=True, max_length=16)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='numman.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('permissions', models.ManyToManyField(to='numman.permission')),
                ('typeofservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='numman.typeofservice')),
            ],
        ),
    ]