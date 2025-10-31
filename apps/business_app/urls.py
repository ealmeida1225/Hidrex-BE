# from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter

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
]

urlpatterns += router.urls
