from django.contrib import admin

from apps.business_app.models.diary_precipitation_classification import (
    DiaryPrecipitationClassification,
)
from apps.business_app.models.month_statistics import MonthStatistics
from apps.business_app.models.pluviometer_type import PluviometerType
from apps.business_app.models.precipitation_concentration_index_by_area import (
    PrecipitationConcentrationIndexByArea,
)
from apps.business_app.models.area import Area
from apps.business_app.models.area_node import AreaNode
from apps.business_app.models.area_type import AreaType
from apps.business_app.models.pluviometer import Pluviometer
from apps.business_app.models.precipitation_concentration_index_by_pluviometer import (
    PrecipitationConcentrationIndexByPluviometer,
)
from apps.business_app.models.precipitation_concentration_index_monthly_by_area import (
    PrecipitationConcentrationIndexMonthlyByArea,
)
from apps.business_app.models.precipitation_concentration_index_monthly_by_pluviometer import (
    PrecipitationConcentrationIndexMonthlyByPluviometer,
)
from apps.business_app.models.registers import Registers
from apps.business_app.models.year_statistics import YearStatistics


@admin.register(Pluviometer)
class PluviometerAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "name",
        "lat",
        "lon",
        "station_name",
        "msnm",
        "pluviometer_type",
    ]
    fields = [
        "name",
        "lat",
        "lon",
        "station_name",
        "msnm",
        "pluviometer_type",
    ]


@admin.register(PluviometerType)
class PluviometertypeAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "name",
        "description",
    ]
    fields = [
        "name",
        "description",
    ]


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "name",
        "sub_name",
        "area_type",
        "description",
        "centroid_lat",
        "centroid_lon",
    ]
    fields = [
        "name",
        "sub_name",
        "area_type",
        "description",
        "centroid_lat",
        "centroid_lon",
    ]


@admin.register(AreaNode)
class AreanodeAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "lat",
        "lon",
        "step",
        "area",
    ]
    fields = [
        "lat",
        "lon",
        "step",
        "area",
    ]


@admin.register(AreaType)
class AreatypeAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "name",
        "representation",
        "description",
    ]
    fields = [
        "name",
        "representation",
        "description",
    ]


@admin.register(DiaryPrecipitationClassification)
class DiaryprecipitationclassificationAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "lower_limmit",
        "upper_limmit",
        "classification",
    ]
    fields = [
        "lower_limmit",
        "upper_limmit",
        "classification",
    ]


@admin.register(MonthStatistics)
class MonthStatisticsAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "max_registered_value",
        "total_precipit",
        "year",
        "month",
        "variance",
        "standard_deviation",
        "rainy_streak_med_long",
        "rainy_streak_count",
        "rainy_days_count",
        "daily_mean",
    ]
    fields = [
        "max_registered_value",
        "total_precipit",
        "year",
        "month",
        "variance",
        "standard_deviation",
        "rainy_streak_med_long",
        "rainy_streak_count",
        "rainy_days_count",
        "daily_mean",
    ]


@admin.register(PrecipitationConcentrationIndexByArea)
class PrecipitationConcentrationIndexByAreaAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "area",
        "years_considered",
        "a_value",
        "b_value",
        "r_2_value",
        "ci_value",
        "rainy_days",
        "max_rain_value",
        "rainy_days_percent",
        "rain_by_period_avg",
        "rainy_days_by_period_avg",
        "total_rain_value",
    ]
    fields = [
        "area",
        "years_considered",
        "a_value",
        "b_value",
        "r_2_value",
        "ci_value",
        "rainy_days",
        "max_rain_value",
        "rainy_days_percent",
        "rain_by_period_avg",
        "rainy_days_by_period_avg",
        "total_rain_value",
    ]


@admin.register(PrecipitationConcentrationIndexByPluviometer)
class PrecipitationConcentrationIndexByPluviometerAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "pluviometer",
        "years_considered",
        "a_value",
        "b_value",
        "r_2_value",
        "ci_value",
        "rainy_days",
        "total_rain_value",
        "max_rain_value",
        "rainy_days_percent",
        "rain_by_period_avg",
        "rainy_days_by_period_avg",
    ]
    fields = [
        "pluviometer",
        "years_considered",
        "a_value",
        "b_value",
        "r_2_value",
        "ci_value",
        "rainy_days",
        "total_rain_value",
        "max_rain_value",
        "rainy_days_percent",
        "rain_by_period_avg",
        "rainy_days_by_period_avg",
    ]


@admin.register(PrecipitationConcentrationIndexMonthlyByArea)
class PrecipitationconcentrationIndexMonthlyByAreaAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "area",
        "month",
        "years_considered",
        "a_value",
        "b_value",
        "r_2_value",
        "ci_value",
        "rainy_days",
        "total_rain_value",
        "max_rain_value",
        "rainy_days_percent",
        "rain_by_period_avg",
        "rainy_days_by_period_avg",
    ]
    fields = [
        "area",
        "years_considered",
        "a_value",
        "b_value",
        "r_2_value",
        "ci_value",
        "rainy_days",
        "total_rain_value",
        "max_rain_value",
        "rainy_days_percent",
        "rain_by_period_avg",
        "rainy_days_by_period_avg",
        "month",
    ]


@admin.register(PrecipitationConcentrationIndexMonthlyByPluviometer)
class PrecipitationconcentrationIndexMonthlyByPluviometerAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "pluviometer",
        "month",
        "years_considered",
        "a_value",
        "b_value",
        "r_2_value",
        "ci_value",
        "rainy_days",
        "total_rain_value",
        "max_rain_value",
        "rainy_days_percent",
        "rain_by_period_avg",
        "rainy_days_by_period_avg",
    ]
    fields = [
        "pluviometer",
        "month",
        "years_considered",
        "a_value",
        "b_value",
        "r_2_value",
        "ci_value",
        "rainy_days",
        "total_rain_value",
        "max_rain_value",
        "rainy_days_percent",
        "rain_by_period_avg",
        "rainy_days_by_period_avg",
    ]


@admin.register(Registers)
class RegistersAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "pluviometer",
        "register_date",
        "rain_value",
    ]
    fields = [
        "pluviometer",
        "register_date",
        "rain_value",
    ]


@admin.register(YearStatistics)
class YearStatisticsAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "pluviometer",
        "year",
        "total_precipit",
        "max_registered_value",
        "daily_mean",
        "rainy_days_count",
        "rainy_streak_count",
        "rainy_streak_med_long",
    ]
    fields = [
        "pluviometer",
        "year",
        "total_precipit",
        "max_registered_value",
        "daily_mean",
        "rainy_days_count",
        "rainy_streak_count",
        "rainy_streak_med_long",
    ]
