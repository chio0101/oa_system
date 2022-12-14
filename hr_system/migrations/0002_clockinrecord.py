# Generated by Django 2.1.2 on 2022-09-26 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClockInRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('morning_enter_time', models.TimeField(null=True)),
                ('morning_leave_time', models.TimeField(null=True)),
                ('afteroon_enter_time', models.TimeField(null=True)),
                ('afteroon_leave_time', models.TimeField(null=True)),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
