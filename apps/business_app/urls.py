# from rest_framework import routers
from django.urls import path
from rest_framework_extensions.routers import ExtendedSimpleRouter

from apps.business_app.views import pages
from apps.business_app.views.area import AreaViewSet
from apps.business_app.views.area_node import AreaNodeViewSet
from apps.business_app.views.area_type import AreaTypeViewSet
from apps.business_app.views.diary_precipitation_classification import (
    DiaryPrecipitationClassificationViewSet,
)
from apps.business_app.views.month_statistics import MonthStatisticsViewSet
from apps.business_app.views.pluviometer import PluviometerViewSet
from apps.business_app.views.pluviometer_area import PluviometerAreaViewSet
from apps.business_app.views.pluviometer_type import PluviometerTypeViewSet
from apps.business_app.views.precipitation_concentration_index_by_area import (
    PrecipitationConcentrationIndexByAreaViewSet,
)
from apps.business_app.views.precipitation_concentration_index_by_pluviometer import (
    PrecipitationConcentrationIndexByPluviometerViewSet,
)
from apps.business_app.views.precipitation_concentration_index_monthly_by_area import (
    PrecipitationConcentrationIndexMonthlyByAreaViewSet,
)
from apps.business_app.views.precipitation_concentration_index_monthly_by_pluviometer import (
    PrecipitationConcentrationIndexMonthlyByPluviometerViewSet,
)
from apps.business_app.views.registers import RegistersViewSet
from apps.business_app.views.year_statistics import YearStatisticsViewSet

# from django.urls import path

router = ExtendedSimpleRouter()

router.register(
    "area-node",
    AreaNodeViewSet,
    basename="area-node",
)
router.register(
    "diary-precipitation-classification",
    DiaryPrecipitationClassificationViewSet,
    basename="diary-precipitation-classification",
)
router.register(
    "month-statistics",
    MonthStatisticsViewSet,
    basename="month-statistics",
)
router.register(
    "pluviometer-area",
    PluviometerAreaViewSet,
    basename="pluviometer-area",
)
router.register(
    "pluviometer",
    PluviometerViewSet,
    basename="pluviometer",
)
router.register(
    "pluviometer-type",
    PluviometerTypeViewSet,
    basename="pluviometer-type",
)
router.register(
    "area-type",
    AreaTypeViewSet,
    basename="area-type",
)
router.register(
    "register",
    RegistersViewSet,
    basename="register",
)
router.register(
    "year-statistics",
    YearStatisticsViewSet,
    basename="year-statistics",
)
router.register(
    "precipitation-concentration-index-by-area",
    PrecipitationConcentrationIndexByAreaViewSet,
    basename="precipitation-concentration-index-by-area",
)
router.register(
    "precipitation-concentration-index-by-pluviometer",
    PrecipitationConcentrationIndexByPluviometerViewSet,
    basename="precipitation-concentration-index-by-pluviometer",
)
router.register(
    "precipitation-concentration-index-monthly-by-area",
    PrecipitationConcentrationIndexMonthlyByAreaViewSet,
    basename="precipitation-concentration-index-monthly-by-area",
)
router.register(
    "precipitation-concentration-index-monthly-by-pluviometer",
    PrecipitationConcentrationIndexMonthlyByPluviometerViewSet,
    basename="precipitation-concentration-index-monthly-by-pluviometer",
)

router.register(
    "area",
    AreaViewSet,
    basename="area",
)

urlpatterns = [
    # path("layers/", list_layers, name="list_layers"),
    path("area-type-page/", pages.area_type, name="area-type-page"),
    path("map-page/", pages.map, name="map-page"),
    path("pluviometer-type-page/", pages.pluviometer_type, name="pluviometer-type-page"),
    path("areas-page/", pages.areas, name="areas-page"),
    path(
        "precipitation-concentration-index-by-area-page/",
        pages.precipitation_concentration_index_by_area,
        name="precipitation-concentration-index-by-area-page",
    ),
    path(
        "precipitation-concentration-index-by-pluviometer-page/",
        pages.precipitation_concentration_index_by_pluviometer,
        name="precipitation-concentration-index-by-pluviometer-page",
    ),
    path(
        "precipitation-concentration-index-monthly-by-area-page/",
        pages.precipitation_concentration_index_monthly_by_area,
        name="precipitation-concentration-index-monthly-by-area-page",
    ),
    path(
        "precipitation-concentration-index-monthly-by-pluviometer-page/",
        pages.precipitation_concentration_index_monthly_by_pluviometer,
        name="precipitation-concentration-index-monthly-by-pluviometer-page",
    ),
    path("area-node-page/", pages.area_node, name="area-node-page"),
    path("pluviometer-page/", pages.pluviometer, name="pluviometer-page"),
    path("pluviometer-area-page/", pages.pluviometer_area, name="pluviometer-area-page"),
    path("registers-page/", pages.registers, name="registers-page"),
    path("year-statistics-page/", pages.year_statistics, name="year-statistics-page"),
    path("month-statistics-page/", pages.month_statistics, name="month-statistics-page"),
    path(
        "diary-precipitation-classification-page/",
        pages.diary_precipitation_classification,
        name="diary-precipitation-classification-page",
    ),
]

urlpatterns += router.urls
