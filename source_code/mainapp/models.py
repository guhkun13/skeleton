# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authassignment(models.Model):
    itemname = models.CharField(max_length=64)
    userid = models.CharField(max_length=64)
    bizrule = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AuthAssignment'


class Authitem(models.Model):
    name = models.CharField(max_length=64)
    type = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    bizrule = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AuthItem'


class Authitemchild(models.Model):
    parent = models.CharField(max_length=64)
    child = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'AuthItemChild'


class Rights(models.Model):
    itemname = models.CharField(max_length=64)
    type = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Rights'


class Biller(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    nomor_rekening = models.CharField(max_length=50, blank=True, null=True)
    fee_per_transaksi = models.FloatField()
    api_key = models.CharField(max_length=255, blank=True, null=True)
    penanggung_transaction_fee = models.CharField(max_length=10, blank=True, null=True)
    jenis_biller = models.CharField(max_length=10, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    tipe_biller = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biller'


class Cabang(models.Model):
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabang'


class CabangBiller(models.Model):
    cabang = models.ForeignKey(Cabang, models.DO_NOTHING, primary_key=True)
    biller_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cabang_biller'
        unique_together = (('cabang', 'biller_id'),)


class CabangUser(models.Model):
    cabang = models.ForeignKey(Cabang, models.DO_NOTHING, primary_key=True)
    user_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cabang_user'
        unique_together = (('cabang', 'user_id'),)


class FlaggingHistory(models.Model):
    log_id = models.IntegerField(primary_key=True)
    ts = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    kode_bank = models.CharField(max_length=10, blank=True, null=True)
    kode_biller = models.ForeignKey(Biller, models.DO_NOTHING, db_column='kode_biller', blank=True, null=True)
    nomor_pembayaran = models.CharField(max_length=50, blank=True, null=True)
    tgl_trx_ca = models.CharField(max_length=30, blank=True, null=True)
    id_trx = models.CharField(max_length=50, blank=True, null=True)
    no_jurnal = models.CharField(max_length=50, blank=True, null=True)
    nominal_bayar = models.CharField(max_length=50, blank=True, null=True)
    billref = models.CharField(max_length=50, blank=True, null=True)
    rc = models.CharField(max_length=2, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    ts_resp = models.DateTimeField(blank=True, null=True)
    nama = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flagging_history'


class LogBlastNotif(models.Model):
    id = models.BigAutoField(primary_key=True)
    billerid = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    tipe = models.CharField(max_length=100, blank=True, null=True)
    banyak_data = models.IntegerField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_blast_notif'


class LogInquiry(models.Model):
    log_id = models.IntegerField(primary_key=True)
    ts = models.DateTimeField()
    kode_biller = models.CharField(max_length=10)
    kode_bank = models.CharField(max_length=10, blank=True, null=True)
    kode_channel = models.CharField(max_length=20, blank=True, null=True)
    nama_channel = models.CharField(max_length=100, blank=True, null=True)
    kode_terminal = models.CharField(max_length=50, blank=True, null=True)
    nomor_pembayaran = models.CharField(max_length=50, blank=True, null=True)
    tgl_trx_ca = models.CharField(max_length=30, blank=True, null=True)
    id_trx = models.CharField(max_length=50, blank=True, null=True)
    rc = models.CharField(max_length=2, blank=True, null=True)
    id_tagihan = models.CharField(max_length=100, blank=True, null=True)
    catatan = models.CharField(max_length=255, blank=True, null=True)
    info_1 = models.CharField(max_length=255, blank=True, null=True)
    info_2 = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_inquiry'
        unique_together = (('log_id', 'kode_biller'),)


class LogNotifEmail(models.Model):
    billerid = models.CharField(max_length=10)
    id_tagihan = models.CharField(max_length=30)
    id_record_pembayaran = models.CharField(max_length=30, blank=True, null=True)
    nomor_pembayaran = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    category = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    sender = models.CharField(max_length=50, blank=True, null=True)
    tipe = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_notif_email'


class LogPayment(models.Model):
    log_id = models.IntegerField()
    ts = models.DateTimeField()
    kode_bank = models.CharField(max_length=10, blank=True, null=True)
    kode_channel = models.CharField(max_length=20, blank=True, null=True)
    nama_channel = models.CharField(max_length=100, blank=True, null=True)
    kode_terminal = models.CharField(max_length=50, blank=True, null=True)
    kode_biller = models.CharField(primary_key=True, max_length=10)
    nomor_pembayaran = models.CharField(max_length=50, blank=True, null=True)
    tgl_trx_ca = models.CharField(max_length=30, blank=True, null=True)
    nominal_tagihan = models.FloatField(blank=True, null=True)
    nominal_bayar = models.FloatField(blank=True, null=True)
    id_trx = models.CharField(max_length=50, blank=True, null=True)
    no_jurnal = models.CharField(max_length=50, blank=True, null=True)
    billref = models.CharField(max_length=50, blank=True, null=True)
    rc = models.CharField(max_length=2, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    info_1 = models.CharField(max_length=100, blank=True, null=True)
    info_2 = models.CharField(max_length=100, blank=True, null=True)
    rekening = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_payment'
        unique_together = (('kode_biller', 'log_id'),)


class LogReversal(models.Model):
    ts = models.DateTimeField()
    seq = models.BigIntegerField(primary_key=True)
    kode_biller = models.CharField(max_length=10)
    kode_bank = models.CharField(max_length=10)
    kode_channel = models.CharField(max_length=20)
    nama_channel = models.CharField(max_length=30, blank=True, null=True)
    kode_terminal = models.CharField(max_length=50, blank=True, null=True)
    id_trx = models.CharField(max_length=50, blank=True, null=True)
    tgl_trx_ca = models.CharField(max_length=30, blank=True, null=True)
    tgl_trx_ca_asal = models.CharField(max_length=30, blank=True, null=True)
    no_jurnal = models.CharField(max_length=100)
    nomor_pembayaran = models.CharField(max_length=50)
    total_nominal = models.CharField(max_length=50, blank=True, null=True)
    billref = models.CharField(max_length=20, blank=True, null=True)
    rc = models.CharField(max_length=2, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    komentar = models.CharField(max_length=100, blank=True, null=True)
    nama = models.CharField(max_length=100, blank=True, null=True)
    id_tagihan = models.CharField(max_length=50, blank=True, null=True)
    payment_request_id = models.CharField(max_length=50, blank=True, null=True)
    reversal_request_id = models.CharField(max_length=50, blank=True, null=True)
    ts_resp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_reversal'


class LogUpload(models.Model):
    id_csvuploads = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    billerid = models.IntegerField()
    namafile = models.CharField(max_length=100, blank=True, null=True)
    uploaddate = models.CharField(max_length=30, blank=True, null=True)
    savetodbdate = models.CharField(max_length=30, blank=True, null=True)
    deletedate = models.CharField(max_length=30, blank=True, null=True)
    kode_upload = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_upload'


class Lookup(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lookup'


class Payment(models.Model):
    ts = models.DateTimeField()
    seq = models.BigIntegerField(primary_key=True)
    kode_biller = models.CharField(max_length=10)
    nama_biller = models.CharField(max_length=100, blank=True, null=True)
    kode_bank = models.CharField(max_length=20)
    kode_channel = models.CharField(max_length=30)
    nama_channel = models.CharField(max_length=100, blank=True, null=True)
    kode_terminal = models.CharField(max_length=50, blank=True, null=True)
    id_trx = models.CharField(max_length=100)
    tgl_trx_ca = models.CharField(max_length=100)
    nama = models.CharField(max_length=255)
    nomor_pembayaran = models.CharField(max_length=100)
    nominal_bayar = models.FloatField()
    status_bayar = models.SmallIntegerField(blank=True, null=True)
    no_jurnal = models.CharField(max_length=100)
    rc = models.CharField(max_length=10, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    komentar = models.CharField(max_length=100, blank=True, null=True)
    id_tagihan = models.CharField(max_length=100, blank=True, null=True)
    rekening = models.CharField(max_length=50, blank=True, null=True)
    status_settlement = models.SmallIntegerField(blank=True, null=True)
    billref = models.CharField(max_length=100, blank=True, null=True)
    subbiller = models.CharField(max_length=10, blank=True, null=True)
    invoice_ke = models.IntegerField(blank=True, null=True)
    id_record_rekonsiliasi = models.CharField(max_length=30, blank=True, null=True)
    id_record_settlement = models.CharField(max_length=30, blank=True, null=True)
    info_key_1 = models.CharField(max_length=50, blank=True, null=True)
    info_value_1 = models.CharField(max_length=100, blank=True, null=True)
    info_key_2 = models.CharField(max_length=50, blank=True, null=True)
    info_value_2 = models.CharField(max_length=100, blank=True, null=True)
    info_key_3 = models.CharField(max_length=50, blank=True, null=True)
    info_value_3 = models.CharField(max_length=100, blank=True, null=True)
    info_key_4 = models.CharField(max_length=50, blank=True, null=True)
    info_value_4 = models.CharField(max_length=100, blank=True, null=True)
    info_key_5 = models.CharField(max_length=50, blank=True, null=True)
    info_value_5 = models.CharField(max_length=100, blank=True, null=True)
    info_key_6 = models.CharField(max_length=50, blank=True, null=True)
    info_value_6 = models.CharField(max_length=100, blank=True, null=True)
    info_key_7 = models.CharField(max_length=50, blank=True, null=True)
    info_value_7 = models.CharField(max_length=100, blank=True, null=True)
    info_key_8 = models.CharField(max_length=50, blank=True, null=True)
    info_value_8 = models.CharField(max_length=100, blank=True, null=True)
    info_key_9 = models.CharField(max_length=50, blank=True, null=True)
    info_value_9 = models.CharField(max_length=100, blank=True, null=True)
    info_key_10 = models.CharField(max_length=50, blank=True, null=True)
    info_value_10 = models.CharField(max_length=100, blank=True, null=True)
    kode_rincian_1 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_1 = models.FloatField(blank=True, null=True)
    kode_rincian_2 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_2 = models.FloatField(blank=True, null=True)
    kode_rincian_3 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_3 = models.FloatField(blank=True, null=True)
    kode_rincian_4 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_4 = models.FloatField(blank=True, null=True)
    kode_rincian_5 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_5 = models.FloatField(blank=True, null=True)
    kode_rincian_6 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_6 = models.FloatField(blank=True, null=True)
    kode_rincian_7 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_7 = models.FloatField(blank=True, null=True)
    kode_rincian_8 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_8 = models.FloatField(blank=True, null=True)
    kode_rincian_9 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_9 = models.FloatField(blank=True, null=True)
    kode_rincian_10 = models.CharField(max_length=100, blank=True, null=True)
    nominal_rincian_10 = models.FloatField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Pembayaran(models.Model):
    ts = models.DateTimeField()
    id_record_pembayaran = models.CharField(primary_key=True, max_length=30)
    kode_biller = models.CharField(max_length=10)
    kode_bank = models.CharField(max_length=10)
    kode_channel = models.CharField(max_length=25)
    nama_channel = models.CharField(max_length=25, blank=True, null=True)
    kode_terminal = models.CharField(max_length=25, blank=True, null=True)
    id_trx = models.CharField(max_length=50)
    tgl_trx_ca = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    nomor_pembayaran = models.CharField(max_length=30)
    nominal_bayar = models.FloatField()
    id_tagihan = models.CharField(max_length=50)
    status_bayar = models.IntegerField()
    no_jurnal = models.CharField(max_length=100)
    id_record_rekonsiliasi = models.CharField(max_length=30, blank=True, null=True)
    id_record_settlement = models.CharField(max_length=30, blank=True, null=True)
    billref = models.CharField(max_length=30, blank=True, null=True)
    metode_pembayaran = models.CharField(max_length=20, blank=True, null=True)
    catatan = models.CharField(max_length=200, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pembayaran'


class Tagihan(models.Model):
    billerid = models.CharField(primary_key=True, max_length=10)
    id_tagihan = models.CharField(max_length=100)
    nomor_pembayaran = models.CharField(max_length=30)
    is_tagihan_aktif = models.IntegerField()
    waktu_berlaku = models.DateTimeField(blank=True, null=True)
    waktu_berakhir = models.DateTimeField(blank=True, null=True)
    urutan_antrian = models.IntegerField()
    nomor_induk = models.CharField(max_length=30, blank=True, null=True)
    nama = models.CharField(max_length=255, blank=True, null=True)
    fakultas = models.CharField(max_length=255, blank=True, null=True)
    jurusan = models.CharField(max_length=255, blank=True, null=True)
    strata = models.CharField(max_length=255, blank=True, null=True)
    periode = models.CharField(max_length=255, blank=True, null=True)
    angkatan = models.CharField(max_length=255, blank=True, null=True)
    total_nominal_tagihan = models.FloatField()
    kode_rincian_1 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_1 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_1 = models.FloatField(blank=True, null=True)
    kode_rincian_2 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_2 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_2 = models.FloatField(blank=True, null=True)
    kode_rincian_3 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_3 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_3 = models.FloatField(blank=True, null=True)
    kode_rincian_4 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_4 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_4 = models.FloatField(blank=True, null=True)
    kode_rincian_5 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_5 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_5 = models.FloatField(blank=True, null=True)
    kode_rincian_6 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_6 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_6 = models.FloatField(blank=True, null=True)
    kode_rincian_7 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_7 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_7 = models.FloatField(blank=True, null=True)
    kode_rincian_8 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_8 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_8 = models.FloatField(blank=True, null=True)
    kode_rincian_9 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_9 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_9 = models.FloatField(blank=True, null=True)
    kode_rincian_10 = models.CharField(max_length=10, blank=True, null=True)
    deskripsi_rincian_10 = models.CharField(max_length=255, blank=True, null=True)
    nominal_rincian_10 = models.FloatField(blank=True, null=True)
    status_bayar = models.IntegerField()
    nomor_hp = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    invoice_ke = models.IntegerField(blank=True, null=True)
    info_1 = models.CharField(max_length=100, blank=True, null=True)
    info_2 = models.CharField(max_length=100, blank=True, null=True)
    kode_bayar_va = models.CharField(max_length=10, blank=True, null=True)
    kode_upload = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.CharField(max_length=100, blank=True, null=True)
    updatedby = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tagihan'
        unique_together = (('billerid', 'id_tagihan'),)


class UnflaggingHistory(models.Model):
    log_id = models.IntegerField(primary_key=True)
    ts = models.DateTimeField()
    bank = models.CharField(max_length=10, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    biller_id = models.CharField(max_length=10, blank=True, null=True)
    id_byr = models.CharField(max_length=50, blank=True, null=True)
    tgl_trx_ca = models.CharField(max_length=30, blank=True, null=True)
    tgl_trx_ca_asal = models.CharField(max_length=30, blank=True, null=True)
    total_nominal = models.CharField(max_length=50, blank=True, null=True)
    id_trx = models.CharField(max_length=50, blank=True, null=True)
    no_jurnal = models.CharField(max_length=50, blank=True, null=True)
    rc = models.CharField(max_length=2, blank=True, null=True)
    ts_resp = models.DateTimeField(blank=True, null=True)
    komentar = models.CharField(max_length=500, blank=True, null=True)
    env = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unflagging_history'


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    userpass = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    biller_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserBiller(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    biller_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user_biller'
        unique_together = (('username', 'biller_id'),)
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Mapping(models.Model):
    kode_biller = models.CharField(primary_key=True, max_length=10)
    nama_biller = models.CharField(max_length=100)
    tipe_biller = models.CharField(max_length=10)
    tipe_bayar = models.CharField(max_length=50, blank=True, null=True)
    url_inquiry = models.CharField(max_length=200, blank=True, null=True)
    url_payment = models.CharField(max_length=200, blank=True, null=True)
    url_reversal = models.CharField(max_length=200, blank=True, null=True)
    catatan = models.TextField(blank=True, null=True)
    creator = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapping'
