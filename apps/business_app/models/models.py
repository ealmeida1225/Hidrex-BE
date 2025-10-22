# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ResearchArea(models.Model):
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    centroid_lat = models.FloatField()
    area_type = models.ForeignKey('ResearchAreatype', models.DO_NOTHING)
    centroid_lon = models.FloatField()

    class Meta:
        managed = False
        db_table = 'research_area'


class ResearchAreanode(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    step = models.IntegerField()
    area = models.ForeignKey(ResearchArea, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_areanode'


class ResearchAreatype(models.Model):
    name = models.CharField(max_length=50)
    representation = models.CharField(max_length=7)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'research_areatype'


class ResearchDiaryprecipitationclassification(models.Model):
    lower_limmit = models.FloatField(blank=True, null=True)
    upper_limmit = models.FloatField(blank=True, null=True)
    classification = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'research_diaryprecipitationclassification'


class ResearchMonthstatistics(models.Model):
    max_registered_value = models.FloatField()
    daily_mean = models.FloatField()
    rainy_days_count = models.PositiveIntegerField()
    rainy_streak_count = models.IntegerField()
    rainy_streak_med_long = models.FloatField()
    standard_deviation = models.FloatField()
    variance = models.FloatField()
    month = models.PositiveSmallIntegerField()
    year = models.ForeignKey('ResearchYearstatistics', models.DO_NOTHING)
    total_precipit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'research_monthstatistics'


class ResearchPluviometer(models.Model):
    name = models.CharField(max_length=15)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    station_name = models.CharField(max_length=100, blank=True, null=True)
    msnm = models.IntegerField(blank=True, null=True)
    pluviometer_type = models.ForeignKey('ResearchPluviometertype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'research_pluviometer'


class ResearchPluviometerarea(models.Model):
    area = models.ForeignKey(ResearchArea, models.DO_NOTHING)
    pluviometer = models.ForeignKey(ResearchPluviometer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_pluviometerarea'


class ResearchPluviometertype(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'research_pluviometertype'


class ResearchPrecipitationconcentrationindexbyarea(models.Model):
    years_considered = models.PositiveSmallIntegerField()
    a_value = models.FloatField()
    b_value = models.FloatField()
    r_2_value = models.FloatField()
    ci_value = models.FloatField()
    rainy_days = models.PositiveIntegerField()
    max_rain_value = models.FloatField()
    rainy_days_percent = models.FloatField()
    rain_by_period_avg = models.FloatField()
    rainy_days_by_period_avg = models.TextField()
    area = models.ForeignKey(ResearchArea, models.DO_NOTHING)
    total_rain_value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'research_precipitationconcentrationindexbyarea'


class ResearchPrecipitationconcentrationindexbypluviometer(models.Model):
    years_considered = models.PositiveSmallIntegerField()
    a_value = models.FloatField()
    b_value = models.FloatField()
    r_2_value = models.FloatField()
    ci_value = models.FloatField()
    rainy_days = models.PositiveIntegerField()
    total_rain_value = models.FloatField()
    max_rain_value = models.FloatField()
    rainy_days_percent = models.FloatField()
    rain_by_period_avg = models.FloatField()
    rainy_days_by_period_avg = models.TextField()
    pluviometer = models.ForeignKey(ResearchPluviometer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_precipitationconcentrationindexbypluviometer'


class ResearchPrecipitationconcentrationindexmonthlybyarea(models.Model):
    years_considered = models.PositiveSmallIntegerField()
    a_value = models.FloatField()
    b_value = models.FloatField()
    r_2_value = models.FloatField()
    ci_value = models.FloatField()
    rainy_days = models.PositiveIntegerField()
    max_rain_value = models.FloatField()
    rainy_days_percent = models.FloatField()
    rain_by_period_avg = models.FloatField()
    rainy_days_by_period_avg = models.TextField()
    month = models.PositiveSmallIntegerField()
    area = models.ForeignKey(ResearchArea, models.DO_NOTHING)
    total_rain_value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'research_precipitationconcentrationindexmonthlybyarea'


class ResearchPrecipitationconcentrationindexmonthlybypluviometer(models.Model):
    years_considered = models.PositiveSmallIntegerField()
    a_value = models.FloatField()
    b_value = models.FloatField()
    r_2_value = models.FloatField()
    ci_value = models.FloatField()
    rainy_days = models.PositiveIntegerField()
    max_rain_value = models.FloatField()
    rainy_days_percent = models.FloatField()
    rain_by_period_avg = models.FloatField()
    rainy_days_by_period_avg = models.TextField()
    month = models.PositiveSmallIntegerField()
    pluviometer = models.ForeignKey(ResearchPluviometer, models.DO_NOTHING)
    total_rain_value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'research_precipitationconcentrationindexmonthlybypluviometer'


class ResearchRegisters(models.Model):
    register_date = models.DateField()
    rain_value = models.FloatField()
    pluviometer = models.ForeignKey(ResearchPluviometer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_registers'


class ResearchYearstatistics(models.Model):
    total_precipit = models.FloatField()
    max_registered_value = models.FloatField()
    daily_mean = models.FloatField()
    rainy_days_count = models.PositiveIntegerField()
    rainy_streak_count = models.IntegerField()
    rainy_streak_med_long = models.FloatField()
    pluviometer = models.ForeignKey(ResearchPluviometer, models.DO_NOTHING)
    year = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'research_yearstatistics'