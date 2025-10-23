from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.area_type import AreaType
from apps.business_app.serializers.area_type import AreaTypeSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class AreaTypeViewSet(viewsets.ModelViewSet, GenericAPIView):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = AreaType.objects.all()
    serializer_class = AreaTypeSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
