# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class LogRekon(models.Model):
    seq = models.BigIntegerField(primary_key=True)
    ts = models.DateTimeField()
    kode_biller = models.CharField(max_length=10, blank=True, null=True)
    kode_bayar = models.CharField(max_length=10, blank=True, null=True)
    tanggal_mulai = models.CharField(max_length=10, blank=True, null=True)
    tanggal_akhir = models.CharField(max_length=10, blank=True, null=True)
    nominal_rekon = models.CharField(max_length=20, blank=True, null=True)
    rc = models.CharField(max_length=20, blank=True, null=True)
    response_msg = models.CharField(max_length=200, blank=True, null=True)
    msg_outgoing = models.TextField(blank=True, null=True)
    msg_incoming = models.TextField(blank=True, null=True)
    mti = models.CharField(max_length=10, blank=True, null=True)
    bit2 = models.CharField(max_length=50, blank=True, null=True)
    bit3 = models.CharField(max_length=50, blank=True, null=True)
    bit4 = models.CharField(max_length=50, blank=True, null=True)
    bit7 = models.CharField(max_length=50, blank=True, null=True)
    bit11 = models.CharField(max_length=50, blank=True, null=True)
    bit12 = models.CharField(max_length=50, blank=True, null=True)
    bit13 = models.CharField(max_length=50, blank=True, null=True)
    bit18 = models.CharField(max_length=50, blank=True, null=True)
    bit28 = models.CharField(max_length=50, blank=True, null=True)
    bit32 = models.CharField(max_length=50, blank=True, null=True)
    bit37 = models.CharField(max_length=50, blank=True, null=True)
    bit39 = models.CharField(max_length=50, blank=True, null=True)
    bit41 = models.CharField(max_length=50, blank=True, null=True)
    bit43 = models.CharField(max_length=50, blank=True, null=True)
    bit48 = models.TextField(blank=True, null=True)
    bit49 = models.CharField(max_length=50, blank=True, null=True)
    bit63 = models.CharField(max_length=200, blank=True, null=True)
    ts_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_rekon'


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
    catatan = models.CharField(max_length=255, blank=True, null=True)
    komentar = models.CharField(max_length=255, blank=True, null=True)
    nama = models.CharField(max_length=200, blank=True, null=True)
    id_tagihan = models.CharField(max_length=50, blank=True, null=True)
    payment_request_id = models.CharField(max_length=50, blank=True, null=True)
    reversal_request_id = models.CharField(max_length=50, blank=True, null=True)
    ts_resp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_reversal'


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
    komentar = models.CharField(max_length=255, blank=True, null=True)
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
        unique_together = (('seq', 'seq'),)

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

