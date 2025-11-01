from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.precipitation_concentration_index_monthly_by_pluviometer import (
    PrecipitationConcentrationIndexMonthlyByPluviometer,
)
from apps.business_app.serializers.precipitation_concentration_index_monthly_by_pluviometer import (
    PrecipitationConcentrationIndexMonthlyByPluviometerSerializer,
)
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class PrecipitationConcentrationIndexMonthlyByPluviometerViewSet(
    viewsets.ModelViewSet, GenericAPIView
):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = PrecipitationConcentrationIndexMonthlyByPluviometer.objects.all().select_related(
        "pluviometer"
    )
    serializer_class = PrecipitationConcentrationIndexMonthlyByPluviometerSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
