# Generated by Django 2.2.11 on 2020-05-23 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authassignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=64)),
                ('userid', models.CharField(max_length=64)),
                ('bizrule', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'AuthAssignment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('bizrule', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'AuthItem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authitemchild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=64)),
                ('child', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'AuthItemChild',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Biller',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('nomor_rekening', models.CharField(blank=True, max_length=50, null=True)),
                ('fee_per_transaksi', models.FloatField()),
                ('api_key', models.CharField(blank=True, max_length=255, null=True)),
                ('penanggung_transaction_fee', models.CharField(blank=True, max_length=10, null=True)),
                ('jenis_biller', models.CharField(blank=True, max_length=10, null=True)),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'biller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cabang',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cabang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FlaggingHistory',
            fields=[
                ('log_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ts', models.DateTimeField()),
                ('kode_bank', models.CharField(blank=True, max_length=10, null=True)),
                ('nomor_pembayaran', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_trx_ca', models.CharField(blank=True, max_length=30, null=True)),
                ('id_trx', models.CharField(blank=True, max_length=50, null=True)),
                ('no_jurnal', models.CharField(blank=True, max_length=50, null=True)),
                ('nominal_bayar', models.CharField(blank=True, max_length=50, null=True)),
                ('billref', models.CharField(blank=True, max_length=50, null=True)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('catatan', models.CharField(blank=True, max_length=100, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
                ('nama', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'flagging_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogBlastNotif',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('billerid', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('tipe', models.CharField(blank=True, max_length=100, null=True)),
                ('banyak_data', models.IntegerField(blank=True, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'log_blast_notif',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogInquiry',
            fields=[
                ('log_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ts', models.DateTimeField()),
                ('kode_biller', models.CharField(max_length=10)),
                ('kode_bank', models.CharField(blank=True, max_length=10, null=True)),
                ('kode_channel', models.CharField(blank=True, max_length=20, null=True)),
                ('nama_channel', models.CharField(blank=True, max_length=100, null=True)),
                ('kode_terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('nomor_pembayaran', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_trx_ca', models.CharField(blank=True, max_length=30, null=True)),
                ('id_trx', models.CharField(blank=True, max_length=50, null=True)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('catatan', models.CharField(blank=True, max_length=255, null=True)),
                ('id_tagihan', models.CharField(blank=True, max_length=100, null=True)),
                ('info_1', models.CharField(blank=True, max_length=255, null=True)),
                ('info_2', models.CharField(blank=True, max_length=255, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'log_inquiry',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogNotifEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billerid', models.CharField(max_length=10)),
                ('id_tagihan', models.CharField(max_length=30)),
                ('id_record_pembayaran', models.CharField(blank=True, max_length=30, null=True)),
                ('nomor_pembayaran', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('sender', models.CharField(blank=True, max_length=50, null=True)),
                ('tipe', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'log_notif_email',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogPayment',
            fields=[
                ('log_id', models.IntegerField()),
                ('ts', models.DateTimeField()),
                ('kode_bank', models.CharField(blank=True, max_length=10, null=True)),
                ('kode_channel', models.CharField(blank=True, max_length=20, null=True)),
                ('nama_channel', models.CharField(blank=True, max_length=100, null=True)),
                ('kode_terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('kode_biller', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nomor_pembayaran', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_trx_ca', models.CharField(blank=True, max_length=30, null=True)),
                ('nominal_tagihan', models.FloatField(blank=True, null=True)),
                ('nominal_bayar', models.FloatField(blank=True, null=True)),
                ('id_trx', models.CharField(blank=True, max_length=50, null=True)),
                ('no_jurnal', models.CharField(blank=True, max_length=50, null=True)),
                ('billref', models.CharField(blank=True, max_length=50, null=True)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('catatan', models.CharField(blank=True, max_length=100, null=True)),
                ('info_1', models.CharField(blank=True, max_length=100, null=True)),
                ('info_2', models.CharField(blank=True, max_length=100, null=True)),
                ('rekening', models.CharField(blank=True, max_length=50, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'log_payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogReversal',
            fields=[
                ('ts', models.DateTimeField()),
                ('seq', models.BigIntegerField(primary_key=True, serialize=False)),
                ('kode_biller', models.CharField(max_length=10)),
                ('kode_bank', models.CharField(max_length=10)),
                ('kode_channel', models.CharField(max_length=20)),
                ('nama_channel', models.CharField(blank=True, max_length=30, null=True)),
                ('kode_terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_trx', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_trx_ca', models.CharField(blank=True, max_length=30, null=True)),
                ('tgl_trx_ca_asal', models.CharField(blank=True, max_length=30, null=True)),
                ('no_jurnal', models.CharField(max_length=100)),
                ('nomor_pembayaran', models.CharField(max_length=50)),
                ('total_nominal', models.CharField(blank=True, max_length=50, null=True)),
                ('billref', models.CharField(blank=True, max_length=20, null=True)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('catatan', models.CharField(blank=True, max_length=100, null=True)),
                ('komentar', models.CharField(blank=True, max_length=100, null=True)),
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
                ('id_tagihan', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_request_id', models.CharField(blank=True, max_length=50, null=True)),
                ('reversal_request_id', models.CharField(blank=True, max_length=50, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'log_reversal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogUpload',
            fields=[
                ('id_csvuploads', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('billerid', models.IntegerField()),
                ('namafile', models.CharField(blank=True, max_length=100, null=True)),
                ('uploaddate', models.CharField(blank=True, max_length=30, null=True)),
                ('savetodbdate', models.CharField(blank=True, max_length=30, null=True)),
                ('deletedate', models.CharField(blank=True, max_length=30, null=True)),
                ('kode_upload', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'log_upload',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('position', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lookup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('ts', models.DateTimeField()),
                ('seq', models.BigIntegerField(primary_key=True, serialize=False)),
                ('kode_biller', models.CharField(max_length=10)),
                ('nama_biller', models.CharField(blank=True, max_length=100, null=True)),
                ('kode_bank', models.CharField(max_length=20)),
                ('kode_channel', models.CharField(max_length=30)),
                ('nama_channel', models.CharField(blank=True, max_length=100, null=True)),
                ('kode_terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_trx', models.CharField(max_length=100)),
                ('tgl_trx_ca', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=255)),
                ('nomor_pembayaran', models.CharField(max_length=100)),
                ('nominal_bayar', models.FloatField()),
                ('status_bayar', models.SmallIntegerField(blank=True, null=True)),
                ('no_jurnal', models.CharField(max_length=100)),
                ('rc', models.CharField(blank=True, max_length=10, null=True)),
                ('catatan', models.CharField(blank=True, max_length=100, null=True)),
                ('komentar', models.CharField(blank=True, max_length=100, null=True)),
                ('id_tagihan', models.CharField(blank=True, max_length=100, null=True)),
                ('rekening', models.CharField(blank=True, max_length=50, null=True)),
                ('status_settlement', models.SmallIntegerField(blank=True, null=True)),
                ('billref', models.CharField(blank=True, max_length=100, null=True)),
                ('subbiller', models.CharField(blank=True, max_length=10, null=True)),
                ('invoice_ke', models.IntegerField(blank=True, null=True)),
                ('id_record_rekonsiliasi', models.CharField(blank=True, max_length=30, null=True)),
                ('id_record_settlement', models.CharField(blank=True, max_length=30, null=True)),
                ('info_key_1', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_1', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_2', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_2', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_3', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_3', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_4', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_4', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_5', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_5', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_6', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_6', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_7', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_7', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_8', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_8', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_9', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_9', models.CharField(blank=True, max_length=100, null=True)),
                ('info_key_10', models.CharField(blank=True, max_length=50, null=True)),
                ('info_value_10', models.CharField(blank=True, max_length=100, null=True)),
                ('kode_rincian_1', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_1', models.FloatField(blank=True, null=True)),
                ('kode_rincian_2', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_2', models.FloatField(blank=True, null=True)),
                ('kode_rincian_3', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_3', models.FloatField(blank=True, null=True)),
                ('kode_rincian_4', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_4', models.FloatField(blank=True, null=True)),
                ('kode_rincian_5', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_5', models.FloatField(blank=True, null=True)),
                ('kode_rincian_6', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_6', models.FloatField(blank=True, null=True)),
                ('kode_rincian_7', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_7', models.FloatField(blank=True, null=True)),
                ('kode_rincian_8', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_8', models.FloatField(blank=True, null=True)),
                ('kode_rincian_9', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_9', models.FloatField(blank=True, null=True)),
                ('kode_rincian_10', models.CharField(blank=True, max_length=100, null=True)),
                ('nominal_rincian_10', models.FloatField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('ts', models.DateTimeField()),
                ('id_record_pembayaran', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('kode_biller', models.CharField(max_length=10)),
                ('kode_bank', models.CharField(max_length=10)),
                ('kode_channel', models.CharField(max_length=25)),
                ('nama_channel', models.CharField(blank=True, max_length=25, null=True)),
                ('kode_terminal', models.CharField(blank=True, max_length=25, null=True)),
                ('id_trx', models.CharField(max_length=50)),
                ('tgl_trx_ca', models.CharField(max_length=20)),
                ('nama', models.CharField(max_length=100)),
                ('nomor_pembayaran', models.CharField(max_length=30)),
                ('nominal_bayar', models.FloatField()),
                ('id_tagihan', models.CharField(max_length=50)),
                ('status_bayar', models.IntegerField()),
                ('no_jurnal', models.CharField(max_length=100)),
                ('id_record_rekonsiliasi', models.CharField(blank=True, max_length=30, null=True)),
                ('id_record_settlement', models.CharField(blank=True, max_length=30, null=True)),
                ('billref', models.CharField(blank=True, max_length=30, null=True)),
                ('metode_pembayaran', models.CharField(blank=True, max_length=20, null=True)),
                ('catatan', models.CharField(blank=True, max_length=200, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pembayaran',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=64)),
                ('type', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
            options={
                'db_table': 'Rights',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tagihan',
            fields=[
                ('billerid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('id_tagihan', models.CharField(max_length=100)),
                ('nomor_pembayaran', models.CharField(max_length=30)),
                ('is_tagihan_aktif', models.IntegerField()),
                ('waktu_berlaku', models.DateTimeField(blank=True, null=True)),
                ('waktu_berakhir', models.DateTimeField(blank=True, null=True)),
                ('urutan_antrian', models.IntegerField()),
                ('nomor_induk', models.CharField(blank=True, max_length=30, null=True)),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
                ('fakultas', models.CharField(blank=True, max_length=255, null=True)),
                ('jurusan', models.CharField(blank=True, max_length=255, null=True)),
                ('strata', models.CharField(blank=True, max_length=255, null=True)),
                ('periode', models.CharField(blank=True, max_length=255, null=True)),
                ('angkatan', models.CharField(blank=True, max_length=255, null=True)),
                ('total_nominal_tagihan', models.FloatField()),
                ('kode_rincian_1', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_1', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_1', models.FloatField(blank=True, null=True)),
                ('kode_rincian_2', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_2', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_2', models.FloatField(blank=True, null=True)),
                ('kode_rincian_3', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_3', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_3', models.FloatField(blank=True, null=True)),
                ('kode_rincian_4', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_4', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_4', models.FloatField(blank=True, null=True)),
                ('kode_rincian_5', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_5', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_5', models.FloatField(blank=True, null=True)),
                ('kode_rincian_6', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_6', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_6', models.FloatField(blank=True, null=True)),
                ('kode_rincian_7', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_7', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_7', models.FloatField(blank=True, null=True)),
                ('kode_rincian_8', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_8', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_8', models.FloatField(blank=True, null=True)),
                ('kode_rincian_9', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_9', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_9', models.FloatField(blank=True, null=True)),
                ('kode_rincian_10', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi_rincian_10', models.CharField(blank=True, max_length=255, null=True)),
                ('nominal_rincian_10', models.FloatField(blank=True, null=True)),
                ('status_bayar', models.IntegerField()),
                ('nomor_hp', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('invoice_ke', models.IntegerField(blank=True, null=True)),
                ('info_1', models.CharField(blank=True, max_length=100, null=True)),
                ('info_2', models.CharField(blank=True, max_length=100, null=True)),
                ('kode_bayar_va', models.CharField(blank=True, max_length=10, null=True)),
                ('kode_upload', models.CharField(blank=True, max_length=100, null=True)),
                ('createdby', models.CharField(blank=True, max_length=100, null=True)),
                ('updatedby', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tagihan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnflaggingHistory',
            fields=[
                ('log_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ts', models.DateTimeField()),
                ('bank', models.CharField(blank=True, max_length=10, null=True)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('biller_id', models.CharField(blank=True, max_length=10, null=True)),
                ('id_byr', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_trx_ca', models.CharField(blank=True, max_length=30, null=True)),
                ('tgl_trx_ca_asal', models.CharField(blank=True, max_length=30, null=True)),
                ('total_nominal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_trx', models.CharField(blank=True, max_length=50, null=True)),
                ('no_jurnal', models.CharField(blank=True, max_length=50, null=True)),
                ('rc', models.CharField(blank=True, max_length=2, null=True)),
                ('ts_resp', models.DateTimeField(blank=True, null=True)),
                ('komentar', models.CharField(blank=True, max_length=500, null=True)),
                ('env', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'db_table': 'unflagging_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('userpass', models.CharField(blank=True, max_length=100, null=True)),
                ('fullname', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField()),
                ('biller_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserBiller',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('biller_id', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user_biller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CabangBiller',
            fields=[
                ('cabang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='mainapp.Cabang')),
                ('biller_id', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'cabang_biller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CabangUser',
            fields=[
                ('cabang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='mainapp.Cabang')),
                ('user_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cabang_user',
                'managed': False,
            },
        ),
    ]