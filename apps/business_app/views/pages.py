from django.shortcuts import render

from project_site import settings

# Create your views here.


def area_type(request):
    return render(request, "area_type/area_type.html")


def map(request):
    return render(request, "map/map.html", {"debug_mode": settings.DEBUG})


def map_pluviometer(request, pluviometer_id=None):
    return render(
        request,
        "map/map_pluviometer.html",
        {"pluviometer_id": pluviometer_id, "debug_mode": settings.DEBUG},
    )


def map_area(request):
    return render(
        request, "map/map_area.html", {"debug_mode": settings.DEBUG}
    )


def pluviometer_type(request):
    return render(request, "pluviometer_type/pluviometer_type.html")


def areas(request):
    return render(request, "areas/areas.html")


def precipitation_concentration_index_by_area(request):
    return render(
        request,
        "precipitation_concentration_index_by_area/precipitation_concentration_index_by_area.html",
    )


def precipitation_concentration_index_by_pluviometer_detail(
    request, pluviometer_id=None
):
    return render(
        request,
        "precipitation_concentration_index_by_pluviometer/precipitation_concentration_index_by_pluviometer_detail.html",
        {"pluviometer_id": pluviometer_id},
    )


def precipitation_concentration_index_by_pluviometer(request):
    return render(
        request,
        "precipitation_concentration_index_by_pluviometer/precipitation_concentration_index_by_pluviometer.html",
    )


def precipitation_concentration_index_monthly_by_area(request):
    return render(
        request,
        "precipitation_concentration_index_monthly_by_area/precipitation_concentration_index_monthly_by_area.html",
    )


def precipitation_concentration_index_monthly_by_pluviometer(
    request, pluviometer_id=None
):
    return render(
        request,
        "precipitation_concentration_index_monthly_by_pluviometer/precipitation_concentration_index_monthly_by_pluviometer.html",
        {"pluviometer_id": pluviometer_id},
    )


def area_node(request):
    return render(request, "area_node/area_node.html")


def month_statistics(request, pluviometer_id=None):
    return render(
        request,
        "month_statistics/month_statistics.html",
        {"pluviometer_id": pluviometer_id},
    )


def year_statistics(request, pluviometer_id=None):
    return render(
        request,
        "year_statistics/year_statistics.html",
        {"pluviometer_id": pluviometer_id},
    )


def pluviometer(request):
    return render(request, "pluviometer/pluviometer.html")


def pluviometer_area(request):
    return render(request, "pluviometer_area/pluviometer_area.html")


def diary_precipitation_classification(request):
    return render(
        request,
        "diary_precipitation_classification/diary_precipitation_classification.html",
    )


# def shops(request):
#     return render(request, "shops/shop.html")


# def products(request):
#     return render(request, "products/products.html")


def registers(request):
    return render(request, "registers/registers.html")
