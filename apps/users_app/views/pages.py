from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def usuarios(request):
    return render(request, "user/usuarios.html")


def first_login(request):
    return render(request, "login/login.html")


def register(request):
    return render(request, "login/register.html")


def area_type(request):
    return render(request, "area_type/area_type.html")


def pluviometer_type(request):
    return render(request, "pluviometer_type/pluviometer_type.html")


def areas(request):
    return render(request, "areas/areas.html")


def area_node(request):
    return render(request, "area_node/area_node.html")

def month_statistics(request):
    return render(request, "month_statistics/month_statistics.html")

def year_statistics(request):
    return render(request, "year_statistics/year_statistics.html")


def pluviometer(request):
    return render(request, "pluviometer/pluviometer.html")


def diary_precipitation_classification(request):
    return render(request, "diary_precipitation_classification/diary_precipitation_classification.html")


def shops(request):
    return render(request, "shops/shop.html")


def products(request):
    return render(request, "products/products.html")


def registers(request):
    return render(request, "registers/registers.html")
