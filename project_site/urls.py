"""project_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps.users_app.views import pages

# ...


urlpatterns = [
    # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("user-gestion/", include("apps.users_app.urls")),
    path("business-gestion/", include("apps.business_app.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # path("__debug__/", include("debug_toolbar.urls")),
    path("usuarios/", login_required(pages.usuarios), name="usuarios"),
    path("login/", pages.first_login, name="first_login"),
    path("register/", pages.register, name="register"),
    path("index/", pages.index, name="index"),
    path("", pages.index, name="index"),
    path("area_type/", pages.area_type, name="area_type"),
    path("pluviometer_type/", pages.pluviometer_type, name="pluviometer_type"),
    path("areas/", pages.areas, name="areas"),
    path(
        "precipitation_concentration_index_by_area/",
        pages.precipitation_concentration_index_by_area,
        name="precipitation_concentration_index_by_area",
    ),
    path(
        "precipitation_concentration_index_by_pluviometer/",
        pages.precipitation_concentration_index_by_pluviometer,
        name="precipitation_concentration_index_by_pluviometer",
    ),
    path(
        "precipitation_concentration_index_monthly_by_area/",
        pages.precipitation_concentration_index_monthly_by_area,
        name="precipitation_concentration_index_monthly_by_area",
    ),
    path(
        "precipitation_concentration_index_monthly_by_pluviometer/",
        pages.precipitation_concentration_index_monthly_by_pluviometer,
        name="precipitation_concentration_index_monthly_by_pluviometer",
    ),
    path("area_node/", pages.area_node, name="area_node"),
    path("pluviometer/", pages.pluviometer, name="pluviometer"),
    path("pluviometer_area/", pages.pluviometer_area, name="pluviometer_area"),
    path("shops/", pages.shops, name="shops"),
    path("products/", pages.products, name="products"),
    path("registers/", pages.registers, name="registers"),
    path("year_statistics/", pages.year_statistics, name="year_statistics"),
    path("month_statistics/", pages.month_statistics, name="month_statistics"),
    path(
        "diary_precipitation_classification/",
        pages.diary_precipitation_classification,
        name="diary_precipitation_classification",
    ),
]

# This is for serving media on development stages
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
