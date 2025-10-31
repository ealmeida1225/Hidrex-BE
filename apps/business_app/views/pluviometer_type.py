from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.pluviometer import Pluviometer
from apps.business_app.models.pluviometer_type import PluviometerType
from apps.business_app.serializers.pluviometer import PluviometerSerializer
from apps.business_app.serializers.pluviometer_type import PluviometerTypeSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class PluviometerTypeViewSet(viewsets.ModelViewSet, GenericAPIView):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = PluviometerType.objects.all()
    serializer_class = PluviometerTypeSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
