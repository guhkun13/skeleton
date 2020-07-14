# Generated by Django 2.2.11 on 2020-05-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogKonverter',
            fields=[
                ('file', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('waktu_mulai', models.DateTimeField(blank=True, null=True)),
                ('waktu_selesai', models.DateTimeField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'log_konverter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MobileNews',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('bank', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mobile_news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MobileUser',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('display_name', models.CharField(blank=True, max_length=100, null=True)),
                ('photo_url', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('device_token', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mobile_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MobileUserBiller',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nomor_pembayaran', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mobile_user_biller',
                'managed': False,
            },
        ),
    ]
