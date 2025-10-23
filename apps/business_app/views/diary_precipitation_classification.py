from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.diary_precipitation_classification import (
    DiaryPrecipitationClassification,
)
from apps.business_app.serializers.diary_precipitation_classification import (
    DiaryPrecipitationClassificationSerializer,
)
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class DiaryPrecipitationClassificationViewSet(viewsets.ModelViewSet, GenericAPIView):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = DiaryPrecipitationClassification.objects.all()
    serializer_class = DiaryPrecipitationClassificationSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
