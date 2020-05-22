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
