# Generated by Django 2.1.4 on 2019-01-16 21:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Cash', max_length=128)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('currency', models.CharField(default='BDT', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.CharField(blank=True, default=uuid.uuid4, max_length=128, primary_key=True, serialize=False, unique=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2019, 1, 16, 21, 46, 30, 228038, tzinfo=utc))),
                ('account', models.CharField(default='Cash', max_length=128)),
                ('type', models.CharField(default='debit', max_length=8)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('remarks', models.CharField(max_length=256)),
            ],
        ),
    ]
