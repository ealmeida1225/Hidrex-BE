from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.month_statistics import MonthStatistics
from apps.business_app.serializers.month_statistics import MonthStatisticsSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class MonthStatisticsViewSet(viewsets.ModelViewSet, GenericAPIView):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = MonthStatistics.objects.all()
    serializer_class = MonthStatisticsSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
