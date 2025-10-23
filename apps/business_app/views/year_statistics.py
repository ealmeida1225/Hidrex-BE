from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.year_statistics import YearStatistics
from apps.business_app.serializers.year_statistics import YearStatisticsSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class YearStatisticsViewSet(viewsets.ModelViewSet, GenericAPIView):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = YearStatistics.objects.all()
    serializer_class = YearStatisticsSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
