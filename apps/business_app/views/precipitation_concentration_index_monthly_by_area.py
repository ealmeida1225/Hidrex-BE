from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.precipitation_concentration_index_monthly_by_area import (
    PrecipitationConcentrationIndexMonthlyByArea,
)
from apps.business_app.serializers.precipitation_concentration_index_monthly_by_area import (
    PrecipitationConcentrationIndexMonthlyByAreaSerializer,
)
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class PrecipitationConcentrationIndexMonthlyByAreaViewSet(
    viewsets.ModelViewSet, GenericAPIView
):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = PrecipitationConcentrationIndexMonthlyByArea.objects.all()
    serializer_class = PrecipitationConcentrationIndexMonthlyByAreaSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
