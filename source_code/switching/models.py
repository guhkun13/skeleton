# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mapping(models.Model):
    kode_biller = models.CharField(primary_key=True, max_length=5)
    nama_biller = models.CharField(max_length=100, blank=True, null=True)
    tipe_biller = models.CharField(max_length=50, blank=True, null=True)
    url_biller = models.CharField(max_length=200, blank=True, null=True)
    info_1 = models.CharField(max_length=100, blank=True, null=True)
    info_2 = models.CharField(max_length=100, blank=True, null=True)
    info_3 = models.CharField(max_length=100, blank=True, null=True)
    nama_folder = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapping'
