# Generated by Django 2.2.11 on 2020-05-25 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetilInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_inq_seq', models.BigIntegerField(blank=True, null=True)),
                ('id_item', models.CharField(max_length=100)),
                ('deskripsi', models.CharField(max_length=100)),
                ('nominal', models.IntegerField()),
            ],
            options={
                'db_table': 'detil_inquiry',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetilItemPembayaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_item', models.CharField(max_length=20)),
                ('deskripsi', models.CharField(max_length=40)),
                ('nominal', models.IntegerField()),
            ],
            options={
                'db_table': 'detil_item_pembayaran',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('ts', models.DateTimeField()),
                ('biller', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=10)),
                ('channel', models.CharField(max_length=12)),
                ('terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_byr', models.CharField(max_length=50)),
                ('tgl_trx_ca', models.CharField(max_length=30)),
                ('id_trx', models.CharField(max_length=50)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
                ('seq', models.BigIntegerField(primary_key=True, serialize=False)),
                ('no_induk', models.CharField(blank=True, max_length=100, null=True)),
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
                ('fakultas', models.CharField(blank=True, max_length=100, null=True)),
                ('jurusan', models.CharField(blank=True, max_length=100, null=True)),
                ('strata', models.CharField(blank=True, max_length=100, null=True)),
                ('periode', models.CharField(blank=True, max_length=100, null=True)),
                ('angkatan', models.CharField(blank=True, max_length=100, null=True)),
                ('id_tagihan', models.CharField(blank=True, max_length=100, null=True)),
                ('subbiller', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'inquiry',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Iso8583',
            fields=[
                ('seq', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ts', models.DateTimeField()),
                ('mti', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit2', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit3', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit4', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit7', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit11', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit12', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit13', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit14', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit15', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit18', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit22', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit32', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit33', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit35', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit37', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit42', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit43', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit48', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit49', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit52', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit60', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit63', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit70', models.CharField(blank=True, max_length=1000, null=True)),
                ('bit90', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'iso8583',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentDetil',
            fields=[
                ('payment_detil_seq', models.BigIntegerField(primary_key=True, serialize=False)),
                ('payment_seq', models.BigIntegerField()),
                ('kode', models.CharField(blank=True, max_length=50, null=True)),
                ('deskripsi_pendek', models.CharField(blank=True, max_length=100, null=True)),
                ('deskripsi_panjang', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal', models.FloatField()),
            ],
            options={
                'db_table': 'payment_detil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reversal',
            fields=[
                ('ts', models.DateTimeField()),
                ('biller', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=10)),
                ('channel', models.CharField(max_length=25)),
                ('terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_byr', models.CharField(max_length=50)),
                ('tgl_trx_ca', models.CharField(max_length=30)),
                ('tgl_trx_ca_asal', models.CharField(max_length=30)),
                ('total_nominal', models.CharField(max_length=50)),
                ('id_trx', models.CharField(max_length=50)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
                ('seq', models.BigIntegerField(primary_key=True, serialize=False)),
                ('subbiller', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'reversal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpcBillerTlu',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('kelas', models.CharField(max_length=20)),
                ('deskripsi', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'spc_biller_tlu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpcInquiry',
            fields=[
                ('ts', models.DateTimeField(primary_key=True, serialize=False)),
                ('biller', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=10)),
                ('channel', models.CharField(max_length=12)),
                ('terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_byr', models.CharField(max_length=50)),
                ('tgl_trx_ca', models.CharField(max_length=30)),
                ('id_trx', models.CharField(max_length=50)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('fak', models.CharField(blank=True, max_length=50, null=True)),
                ('seq', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'spc_inquiry',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpcPayment',
            fields=[
                ('ts', models.DateTimeField(primary_key=True, serialize=False)),
                ('biller', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=10)),
                ('channel', models.CharField(max_length=25)),
                ('terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_byr', models.CharField(max_length=50)),
                ('tgl_trx_ca', models.CharField(max_length=30)),
                ('total_nominal', models.CharField(max_length=50)),
                ('id_trx', models.CharField(max_length=50)),
                ('no_jurnal', models.CharField(max_length=50)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('fak', models.CharField(blank=True, max_length=50, null=True)),
                ('is_bayar', models.SmallIntegerField(blank=True, null=True)),
                ('komentar', models.CharField(blank=True, max_length=500, null=True)),
                ('lokasi_file', models.CharField(blank=True, max_length=120, null=True)),
                ('status_settlement', models.SmallIntegerField(blank=True, null=True)),
                ('billref', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'spc_payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpcRekon',
            fields=[
                ('ts', models.DateTimeField(primary_key=True, serialize=False)),
                ('biller', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=10)),
                ('channel', models.CharField(max_length=25)),
                ('terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_byr', models.CharField(max_length=50)),
                ('tgl_trx_ca', models.CharField(max_length=30)),
                ('total_nominal', models.CharField(max_length=50)),
                ('id_trx', models.CharField(max_length=50)),
                ('no_jurnal', models.CharField(max_length=50)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('fak', models.CharField(blank=True, max_length=50, null=True)),
                ('is_bayar', models.SmallIntegerField(blank=True, null=True)),
                ('komentar', models.CharField(blank=True, max_length=500, null=True)),
                ('lokasi_file', models.CharField(blank=True, max_length=120, null=True)),
                ('status_settlement', models.SmallIntegerField(blank=True, null=True)),
                ('ts_rekon', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'spc_rekon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpcReversal',
            fields=[
                ('ts', models.DateTimeField(primary_key=True, serialize=False)),
                ('biller', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=10)),
                ('channel', models.CharField(max_length=25)),
                ('terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_byr', models.CharField(max_length=50)),
                ('tgl_trx_ca', models.CharField(max_length=30)),
                ('tgl_trx_ca_asal', models.CharField(max_length=30)),
                ('total_nominal', models.CharField(max_length=50)),
                ('id_trx', models.CharField(max_length=50)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('fak', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'spc_reversal',
                'managed': False,
            },
        ),
    ]
