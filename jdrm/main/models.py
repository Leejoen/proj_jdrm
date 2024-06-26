# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Audits(models.Model):
    audit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    auditor = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_of_plant = models.ForeignKey('Plants', models.DO_NOTHING, db_column='number_of_plant', blank=True, null=True)
    brief_description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    report = models.ForeignKey('Report', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'Audits'


class Chat(models.Model):
    name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    number_of_plant = models.ForeignKey('Plants', models.DO_NOTHING, db_column='number_of_plant', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'Chat'


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    auditor = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_of_plant = models.ForeignKey('Plants', models.DO_NOTHING, db_column='number_of_plant', blank=True, null=True)
    short_description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'Events'


class MsreplicationOptions(models.Model):
    optname = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    value = models.BooleanField()
    major_version = models.IntegerField()
    minor_version = models.IntegerField()
    revision = models.IntegerField()
    install_failures = models.IntegerField()

    class Meta:
        db_table = 'MSreplication_options'


class Plants(models.Model):
    name_of_plant = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_of_plant = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'Plants'


class Report(models.Model):
    date = models.DateField(blank=True, null=True)
    number_of_plant = models.ForeignKey(Plants, models.DO_NOTHING, db_column='number_of_plant', blank=True, null=True)
    section = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    evaluation_category = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sub_item_number = models.IntegerField(blank=True, null=True)
    evaluation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    responsible_for_evaluation = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    requirements_of_the_roadmap = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    control_element = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    comments = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    list_of_events_for_the_year = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    performer = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    report_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'Report'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    password = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    lastname = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    firstname = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    number_of_plant = models.ForeignKey(Plants, models.DO_NOTHING, db_column='number_of_plant')
    role = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Users'


class AuditsDev(models.Model):
    description_audit = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_audit = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_of_plant = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'audits_dev'


class AuditsDevManagement(models.Model):
    audits_dev = models.OneToOneField(AuditsDev, models.DO_NOTHING, primary_key=True)  # The composite primary key (audits_dev_id, management_id) found, that is not supported. The first column is selected.
    management = models.ForeignKey('Management', models.DO_NOTHING)

    class Meta:
        db_table = 'audits_dev_management'
        unique_together = (('audits_dev', 'management'),)


class EventDev(models.Model):
    date_metric = models.DateField(blank=True, null=True)
    description_metric = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_metric_audit = models.IntegerField(blank=True, null=True)
    location_metric = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_event = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_metric = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    time_metric = models.TimeField(blank=True, null=True)

    class Meta:
        db_table = 'event_dev'


class Management(models.Model):
    id_audit = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    responsible = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'management'


class ManagementConfig1(models.Model):
    id_management = models.ForeignKey(Management, models.DO_NOTHING, db_column='id_management', blank=True, null=True)
    sub_name_section = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_sub_section = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    estimation = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_events = models.ForeignKey(EventDev, models.DO_NOTHING, db_column='id_events', blank=True, null=True)
    executor = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'management_config_1'


class ManagementConfig2(models.Model):
    id_management = models.ForeignKey(Management, models.DO_NOTHING, db_column='id_management', blank=True, null=True)
    sub_name_section = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_sub_section = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    estimation = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_events = models.ForeignKey(EventDev, models.DO_NOTHING, db_column='id_events', blank=True, null=True)
    executor = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'management_config_2'


class PlantsDev(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_of_plant = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'plants_dev'


class RefreshtokenDev(models.Model):
    id = models.BigIntegerField(primary_key=True)
    expiry_date = models.DateTimeField()
    token = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    user = models.OneToOneField('UsersDev', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'refreshtoken_dev'


class RolesDev(models.Model):
    name = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'roles_dev'


class SptFallbackDb(models.Model):
    xserver_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    xdttm_ins = models.DateTimeField()
    xdttm_last_ins_upd = models.DateTimeField()
    xfallback_dbid = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    dbid = models.SmallIntegerField()
    status = models.SmallIntegerField()
    version = models.SmallIntegerField()

    class Meta:
        db_table = 'spt_fallback_db'


class SptFallbackDev(models.Model):
    xserver_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    xdttm_ins = models.DateTimeField()
    xdttm_last_ins_upd = models.DateTimeField()
    xfallback_low = models.IntegerField(blank=True, null=True)
    xfallback_drive = models.CharField(max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    low = models.IntegerField()
    high = models.IntegerField()
    status = models.SmallIntegerField()
    name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    phyname = models.CharField(max_length=127, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        db_table = 'spt_fallback_dev'


class SptFallbackUsg(models.Model):
    xserver_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    xdttm_ins = models.DateTimeField()
    xdttm_last_ins_upd = models.DateTimeField()
    xfallback_vstart = models.IntegerField(blank=True, null=True)
    dbid = models.SmallIntegerField()
    segmap = models.IntegerField()
    lstart = models.IntegerField()
    sizepg = models.IntegerField()
    vstart = models.IntegerField()

    class Meta:
        db_table = 'spt_fallback_usg'


class SptMonitor(models.Model):
    lastrun = models.DateTimeField()
    cpu_busy = models.IntegerField()
    io_busy = models.IntegerField()
    idle = models.IntegerField()
    pack_received = models.IntegerField()
    pack_sent = models.IntegerField()
    connections = models.IntegerField()
    pack_errors = models.IntegerField()
    total_read = models.IntegerField()
    total_write = models.IntegerField()
    total_errors = models.IntegerField()

    class Meta:
        db_table = 'spt_monitor'


class SupplyChain(models.Model):
    id = models.BigIntegerField(primary_key=True)
    metric = models.IntegerField(blank=True, null=True)
    id_audit = models.IntegerField(blank=True, null=True)
    name_metric = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    responsible = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'supply_chain'


class UserPlants(models.Model):
    user = models.OneToOneField('UsersDev', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, plants_id) found, that is not supported. The first column is selected.
    plants = models.ForeignKey(PlantsDev, models.DO_NOTHING)

    class Meta:
        db_table = 'user_plants'
        unique_together = (('user', 'plants'),)


class UserRoles(models.Model):
    user = models.OneToOneField('UsersDev', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey(RolesDev, models.DO_NOTHING)

    class Meta:
        db_table = 'user_roles'
        unique_together = (('user', 'role'),)


class UsersDev(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lastname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    login = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_of_plant = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'users_dev'
