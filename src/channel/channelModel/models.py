# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class PpnCdmChannel(models.Model):
    chan_id = models.CharField(db_column='CHAN_ID', primary_key=True, max_length=64)  # Field name made lowercase.
    chan_code = models.CharField(db_column='CHAN_CODE', max_length=64)  # Field name made lowercase.
    chan_name = models.CharField(db_column='CHAN_NAME', max_length=64)  # Field name made lowercase.
    chan_attach = models.CharField(db_column='CHAN_ATTACH', max_length=64)  # Field name made lowercase.
    chan_type = models.IntegerField(db_column='CHAN_TYPE')  # Field name made lowercase.
    chan_hd_flag = models.CharField(db_column='CHAN_HD_FLAG', max_length=64)  # Field name made lowercase.
    chan_play_begin_time = models.CharField(db_column='CHAN_PLAY_BEGIN_TIME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    chan_play_end_time = models.CharField(db_column='CHAN_PLAY_END_TIME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    chan_desc = models.CharField(db_column='CHAN_DESC', max_length=1024)  # Field name made lowercase.
    chan_begin_date = models.DateTimeField(db_column='CHAN_BEGIN_DATE')  # Field name made lowercase.
    chan_end_date = models.DateTimeField(db_column='CHAN_END_DATE', blank=True, null=True)  # Field name made lowercase.
    chan_status = models.IntegerField(db_column='CHAN_STATUS')  # Field name made lowercase.
    chan_play_site = models.IntegerField(db_column='CHAN_PLAY_SITE')  # Field name made lowercase.
    chan_play_lang = models.CharField(db_column='CHAN_PLAY_LANG', max_length=128)  # Field name made lowercase.
    chan_cover_zone = models.CharField(db_column='CHAN_COVER_ZONE', max_length=128)  # Field name made lowercase.
    chan_field1 = models.CharField(db_column='CHAN_FIELD1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    chan_field2 = models.CharField(db_column='CHAN_FIELD2', max_length=64, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    create_type = models.IntegerField(db_column='CREATE_TYPE', blank=True, null=True)  # Field name made lowercase.
    create_user = models.CharField(db_column='CREATE_USER', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ppn_cdm_channel'

