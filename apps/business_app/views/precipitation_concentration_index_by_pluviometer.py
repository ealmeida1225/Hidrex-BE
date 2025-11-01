from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.precipitation_concentration_index_by_pluviometer import (
    PrecipitationConcentrationIndexByPluviometer,
)
from apps.business_app.serializers.precipitation_concentration_index_by_pluviometer import (
    PrecipitationConcentrationIndexByPluviometerSerializer,
)
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class PrecipitationConcentrationIndexByPluviometerViewSet(
    viewsets.ModelViewSet, GenericAPIView
):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = (
        PrecipitationConcentrationIndexByPluviometer.objects.all().select_related(
            "pluviometer"
        )
    )
    serializer_class = PrecipitationConcentrationIndexByPluviometerSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
